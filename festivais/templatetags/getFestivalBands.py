from django import template


register = template.Library()

@register.filter
def get_festival_bands(festival):

    bands = festival.bandas.all()
    return bands
