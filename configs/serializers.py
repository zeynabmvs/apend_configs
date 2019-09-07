# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.serializers import ModelSerializer

from configs.models import Config


class ConfigSerializer(ModelSerializer):
    class Meta:
        model = Config
        fields = ['key', 'value', 'jvalue']