from django import template
from artigos.models import Rating

register = template.Library()

@register.filter
def get_article_rating(article):

    rating = Rating.objects.filter(article=article).first()
    return rating
