# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


class CustomViewContextMixin:
    """
    context handler, in creating new admin custom view inherit this mixin
    """

    def set_context(self, request):
        self.context = admin.site.each_context(request)
        self.extra_context()

    def extra_context(self):
        return self.context.update({})

    def update_context(self, dict):
        self.context.update(dict)