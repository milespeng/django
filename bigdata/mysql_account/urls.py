# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'mysql_account'
urlpatterns = [
    url(r'^$', views.show_all(), name='show_all'),
    url(r'^new_account/', views.new_account(), name='new_account')
]
