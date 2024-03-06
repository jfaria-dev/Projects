from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter(name='split', is_safe=True)
@stringfilter
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)

@register.filter(name='zero_number', is_safe=True)
@stringfilter
def zero_number(value):
    """
        Returns the value turned into a list.
    """
    if len(value) == 1:
        return '0' + value
    
    return value