# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [       
    url(r'test/filter/$', views.test_filter, name='test_filter'),
    url(r'tag/filter/$', views.tag_filter, name='tag_filter'),
    url(r'', views.django_filter, name='django_filter'),  # 必须放在最后
    
    
]
