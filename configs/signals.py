# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_delete
from django.dispatch import receiver

from configs.models import Config


# @receiver(post_delete, sender=Config)
# def config_post_delete_receiver(sender, instance, **kwargs):
#     print(instance.key, 'deleted')