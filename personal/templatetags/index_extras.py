from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def navbar(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return 'active'
    return ''

