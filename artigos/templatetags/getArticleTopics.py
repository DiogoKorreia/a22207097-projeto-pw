from django import template
from artigos.models import Topic

register = template.Library()

@register.filter
def get_article_topics(article):

    topics = Topic.objects.filter(article=article).order_by('order')
    return topics
