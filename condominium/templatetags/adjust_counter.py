from django import template

from django.conf import settings


register = template.Library()

@register.filter
def adjust_counter(value, page):
    value, page = int(value), int(page)
    adjusted_value = value + ((page - 1) * settings.RESULTS_PER_PAGE)
    return adjusted_value

