# coding: utf-8

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
register = template.Library()

# split 通过指定分隔符对字符串进行切片, 返回分割后的字符串列表。

# 例子一：返回切片的第一部分   {{ 'mysite/blog/test.mp4' | split_0:'/' }} -->  mysite
@register.filter()
def split_0(value, arg):
    return value.split(arg)[0]

# 例子二：返回切片的最后部分 {{ 'mysite/blog/test.mp4' | split_end:'/' }} -->  test.mp4
@register.filter()
def split_end(value, arg):
    return value.split(arg)[-1]