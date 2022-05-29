from django.urls import translate_url as django_translate_url
from django import template


register = template.Library()


@register.simple_tag(name='translate_url')
def translate_url(request, target='de'):
    url = django_translate_url(request.get_full_path(), target)
    return url
