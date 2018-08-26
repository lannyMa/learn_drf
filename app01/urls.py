#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01 import views

router = DefaultRouter()
router.register(r'', views.GoodsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # path('', TemplateView.as_view(template_name='app01/index.html')),
    # path('login/', views.LoginView.as_view()),
]
