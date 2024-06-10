from django import template
from artigos.models import Article

register = template.Library()

@register.filter
def get_user_articles(user):

    articles = Article.objects.filter(author=user).order_by('title')
    return articles
