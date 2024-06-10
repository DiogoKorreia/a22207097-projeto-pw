from django import template
from artigos.models import Comment

register = template.Library()

@register.filter
def get_article_comments(article):

    comments = Comment.objects.filter(article=article).order_by('created_at')
    return comments
