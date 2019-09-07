from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views import View
from rest_framework import generics
from rest_framework.permissions import AllowAny

from configs.forms import AboutUsForm, GeneralConfigForm, UpdateForm
from configs.models import Config, ClientConfig
from configs.serializers import ConfigSerializer
from core.mixins import CustomViewContextMixin


class ConfigDetailView(generics.RetrieveAPIView):
    """
    CBV view to get config detail by key
    """
    permission_classes = ([AllowAny])
    serializer_class = ConfigSerializer
    lookup_url_kwarg = 'key'
    lookup_field = 'key'
    queryset = Config.objects.filter(key__startswith='client_')


@method_decorator(staff_member_required, name='dispatch')
class BaseListSettingsView(CustomViewContextMixin, View):
    """
    Base setting class for list of editable configs 
    """

    template = None
    queryset = Config.objects.none()

    def get(self, request):
        self.set_context(request)

        self.update_context({
            'items': self.queryset
        })
        return render(request, self.template, self.context)


@method_decorator(staff_member_required, name='dispatch')
class BaseEditSingleSettingsView(CustomViewContextMixin, View):
    """
    Base setting class for list of editable configs 
    """

    template = None
    form_class = None
    redirect_url_name = None
    successful_message = _('Changes applied successfully')

    def get(self, request, pk):
        self.set_context(request)
        obj = Config.objects.get(pk=pk)

        form = self.form_class(initial=obj.jvalue)
        self.update_context({
            'form': form,
            'item': obj,
        })

        return render(request, self.template, self.context)

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = Config.objects.get(pk=pk)

            # todo bug, only save form's fields
            obj.jvalue = form.cleaned_data
            obj.save()

            messages.add_message(request, messages.SUCCESS, self.successful_message)

        return redirect(self.redirect_url_name)


@method_decorator(staff_member_required, name='dispatch')
class BaseMultipleSettingsView(CustomViewContextMixin, View):
    """
    Base setting class for multiple config keys listed
    """

    template = None
    form_class = None
    successful_message = _('Changes applied successfully')
    redirect_url_name = None
    keys = list()

    def get(self, request):
        self.set_context(request)

        dic = {}
        configs = Config.objects.filter(key__in=self.keys)
        for config in configs:
            dic[config.key] = config.value

        form = self.form_class(initial=dic)

        self.update_context({
            'form': form
        })
        return render(request, self.template, self.context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            for item in form.fields:
                value = form.cleaned_data[item]

                config_obj = Config.objects.safe_get(item)

                if config_obj:
                    if value:
                        config_obj.value = value
                        config_obj.save()
                    else:
                        config_obj.delete()
                elif value:
                    Config.objects.create(key=item, value=value)
                else:
                    continue

            messages.add_message(request, messages.SUCCESS, self.successful_message)

        return redirect(self.redirect_url_name)


class GeneralSettings(BaseMultipleSettingsView):
    template = 'general_settings.html'
    form_class = GeneralConfigForm
    redirect_url_name = 'general_settings'
    keys = ['admin_email', 'kn_otp_template_name']


@method_decorator(staff_member_required, name='dispatch')
class BaseSingleSettingView(CustomViewContextMixin, View):
    """
    Base setting class for a single config containing multiple related fields
    """

    template = None
    config_key = None
    form_class = None
    successful_message = _('Changes applied successfully')
    redirect_url_name = None

    def get(self, request):
        self.set_context(request)

        obj, created = Config.objects.get_or_create(key=self.config_key)

        form = self.form_class(initial=obj.jvalue)
        self.update_context({
            'form': form
        })

        return render(request, self.template, self.context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj, created = Config.objects.get_or_create(key=self.config_key)

            obj.jvalue = form.cleaned_data
            obj.save()
            messages.add_message(request, messages.SUCCESS, self.successful_message)

        return redirect(self.redirect_url_name)


class AboutSettingsView(BaseSingleSettingView):
    template = 'about_us_settings.html'
    config_key = 'client_about_page'
    form_class = AboutUsForm
    redirect_url_name = 'about_us_settings'


class UpdateSettingsView(BaseSingleSettingView):
    template = 'update_settings.html'
    config_key = 'client_update'
    form_class = UpdateForm
    redirect_url_name = 'update_settings'

    def extra_context(self):
        return self.context.update({
            'current_app_version': settings.CURRENT_APP_VERSION
        })


class ClientConfigListView(generics.ListAPIView):
    permission_classes = ((AllowAny,))
    serializer_class = ConfigSerializer
    queryset = ClientConfig.objects.all()