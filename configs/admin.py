from django.contrib import admin
from django.utils.translation import ugettext as _

from configs.models import ClientConfig, Config
from core.helpers import admin_field_json_formatted


class ConfigAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    list_display_links = ['id', 'key', 'value']
    readonly_fields = ['value_json_formatted']
    search_fields = ['key', 'value']

    def value_json_formatted(self, obj):
        return admin_field_json_formatted(obj.jvalue)

    value_json_formatted.short_description = _('Json value')


admin.site.register(Config, ConfigAdmin)


class ClientConfigAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    list_display_links = ['id', 'key', 'value']
    readonly_fields = ['value_json_formatted']
    search_fields = ['key', 'value']

    def value_json_formatted(self, obj):
        return admin_field_json_formatted(obj.jvalue)

    value_json_formatted.short_description = _('Json value')


admin.site.register(ClientConfig, ClientConfigAdmin)