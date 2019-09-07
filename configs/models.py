from django.contrib.postgres.fields import JSONField
from django.db import models

from django.utils.translation import ugettext as _


class ConfigManager(models.Manager):
    def safe_get(self, value):
        try:
            obj = self.get(key=value)
            return obj
        except Config.DoesNotExist:
            return None


class Config(models.Model):
    key = models.CharField(_('Key'), max_length=100, unique=True)
    value = models.TextField(_('Value'), null=True, blank=True)
    jvalue = JSONField('Json value', null=True, blank=True)

    objects = ConfigManager()

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = _('Config')
        verbose_name_plural = _('Configs')


class ClientConfigManager(models.Manager):
    def get_queryset(self):
        return super(ClientConfigManager, self).get_queryset().filter(key__startswith='client_')


class ClientConfig(Config):
    objects = ClientConfigManager()

    class Meta:
        proxy = True
        verbose_name = _('Client config')
        verbose_name_plural = _('Client configs')