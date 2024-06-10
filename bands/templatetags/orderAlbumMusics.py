from django import template

register = template.Library()

@register.filter
def order_musics(album):
    return album.musics.all().order_by('title')