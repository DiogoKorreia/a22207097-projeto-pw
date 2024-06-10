from django import template

register = template.Library()

@register.filter
def order_bands(bands):
    return bands.order_by('name')
