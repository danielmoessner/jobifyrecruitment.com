from django.urls import reverse
from django.utils import translation
from django import template

register = template.Library()


@register.simple_tag(name='translate_url')
def translate_url(request, target='de'):
    translation.activate(target)
    url = reverse(request.resolver_match.view_name, args=request.resolver_match.args,
                  kwargs=request.resolver_match.kwargs)
    return url
