# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse,\
    StreamingHttpResponse
from django.contrib.auth.decorators import login_required #使用注意在settings.py中设置 LOGIN_URL = '/login/'
from django.utils.safestring import mark_safe

# http://localhost:8000/
#@login_required
def index(request):           
    meg = 'hello world! '
    return render(request, 'account/index.html', context=locals()) 

def test_filter(request):
    return render(request, 'account/test_filter.html')
   
def tag_filter(request):
    return render(request, 'account/tag_filter.html')

def django_filter(request):
    mystr = "abcdefghijklmnopqrstuvwxyz"
    now_date = datetime.now()
    int_list = [100,56,80,1,2,3,4,5,6,7,8,9,10]
    string = "<h3>hello  world book_ok br</h3>"
    mydict = [{'name': 'python'},{'name': 'java'},{'name': 'c++'},]
    date_time = '2018-06-21 23:59:59'
    link = 'https://www.baidu.com/'
    mylist = ['ok','es','yes','no']
    boolean = 'Yes'
    mark_safe_url = mark_safe("<a href='https://www.baidu.com/'>提交</a>") # 在django模板上可点击的链接
    return render(request, 'account/django_filter.html', context=locals() )
