from django.template import Library
import re

register = Library()


@register.filter
def modphone(str):
    return str[:3] + '****' + str[7:]


@register.filter
def modemail(str):
    str1 = re.search(r'@\w+\.com$',str).group()
    return str[:2] + '****' + str1
