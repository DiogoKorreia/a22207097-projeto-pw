from django import template

register = template.Library()

@register.filter
def order_albums(band):
    return band.albums.all().order_by('-releaseDate')