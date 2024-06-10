from django import forms
from .models import UserProfile, Comment, Rating, Article, Topic

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = '__all__'

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = '__all__'

class RatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = '__all__'

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = '__all__'

class TopicForm(forms.ModelForm):
  class Meta:
    model = Topic
    fields = '__all__'

