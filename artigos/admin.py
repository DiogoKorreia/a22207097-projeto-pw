from django.contrib import admin
from .models import UserProfile, Comment, Rating, Article, Topic


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user', 'content', 'created_at')
    list_filter = ('article', 'user')
    search_fields = ('content',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user', 'rating')
    list_filter = ('article', 'user', 'rating')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('author', 'created_at')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ('title', 'article')