# coding: utf-8

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
register = template.Library()

# 例子一：将字符串中指定的字符串替换为空格
# # 使用装饰器简化代码，默认的过滤器名字就是函数的名字
@register.filter()
def cut_filter(value, arg):
    return value.replace(arg, '')

# 例子二：将字母变成小写
@register.filter()
@stringfilter
def mylower(value):
    return value.lower()

# 例子三：Django自定义过滤器是否会自动转义
# 没有自动转义
@register.filter()
def add_no(value, arg):
    return "%s %s" %(value, arg)

# 有自动转义：is_safe 或者mark_safe
@register.filter(is_safe=True)
def add_yes(value, arg):
    return mark_safe("%s %s" %(value, arg))