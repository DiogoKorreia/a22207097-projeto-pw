from django.urls import path
from .views import articles_view, article_view, user_view


app_name = 'artigos'

urlpatterns = [
    path('', articles_view, name='home'),
    path('article/<int:article_id>', article_view, name='article_view'),
    path('user/<int:user_id>', user_view, name= 'user_view')
]