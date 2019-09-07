# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext as _


class AboutUsForm(forms.Form):
    about_page_us = forms.CharField(widget=forms.Textarea(), required=False, label=_('About us'))
    about_page_instagram = forms.URLField(required=False, label=_('Instagram'))
    about_page_telegram = forms.URLField(required=False, label=_('Telegram'))
    about_page_admin_phone = forms.CharField(required=False, label=_('Admin phone'))
    about_page_admin_email = forms.EmailField(required=False, label=_('Admin email'))
    about_page_website_url = forms.URLField(required=False, label=_('website url'))


class UpdateForm(forms.Form):
    CHOICES = (
        ('none', _('---')),
        ('true', _('True')),
        ('false', _('False')),
    )
    update_title = forms.CharField(required=False, label=_('Title'))
    update_new_version_code = forms.IntegerField(required=False, label=_('New version code'))
    update_force = forms.ChoiceField(initial='none', required=False, choices=CHOICES, label=_('Force'))
    update_description = forms.CharField(widget=forms.Textarea(), required=False, label=_('Description'))
    update_new_features = forms.CharField(widget=forms.Textarea(), required=False, label=_('New features'),
                                          help_text=_('add every feature in a new line'))
    update_apk_link = forms.URLField(required=False, label=_('APK link'))


class GeneralConfigForm(forms.Form):
    kn_otp_template_name = forms.CharField(required=False, label=_('Kavenegar\'s template name for sending otp'))
    admin_email = forms.CharField(required=False, label=_('Admin\'s email'), help_text=_('For placing as sender\'s email'))