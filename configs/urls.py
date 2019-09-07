# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path

from configs import views

urlpatterns = [

    path('admin/settings/general/', views.GeneralSettings.as_view(), name='general_settings'),
    path('admin/settings/about/', views.AboutSettingsView.as_view(), name='about_us_settings'),
    path('admin/settings/update/', views.UpdateSettingsView.as_view(), name='update_settings'),

    # rest api
    path('api/v1/config/detail/<slug:key>/', views.ConfigDetailView.as_view()),
    path('api/v1/configs/', views.ClientConfigListView.as_view()),
]