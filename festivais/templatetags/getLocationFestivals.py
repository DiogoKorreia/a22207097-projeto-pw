from django import template
from festivais.models import Festival

register = template.Library()

@register.filter
def get_location_festivals(localizacao):

    festivais = Festival.objects.filter(localizacao=localizacao).order_by('nome')
    return festivais
