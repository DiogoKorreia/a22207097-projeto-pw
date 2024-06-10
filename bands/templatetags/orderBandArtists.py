from django import template

register = template.Library()

@register.filter
def order_artists(band):
    return band.artists.order_by('firstName')