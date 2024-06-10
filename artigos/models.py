from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User



class UserProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos',default=6)
    name = models.CharField(max_length=100,default='Unknown')
    image = models.ImageField(upload_to='artigos/images', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return f'{self.name}'



class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name}'


class Rating(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f'{self.rating}'


class Article(models.Model):
    title = models.CharField(max_length=100)
    intro = models.TextField(default="")
    content = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Topic(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='topics')
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'