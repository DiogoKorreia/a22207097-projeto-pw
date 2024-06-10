from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, UserProfile
from .forms import ArticleForm
from .decorators import group_required


def articles_view(request):

    articles = Article.objects.all()
    context = {'articles' : articles.order_by('created_at')}

    return render(request,"artigos/articles.html",context)


def article_view(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    context = {
        'article': article
        }

    return render(request,"artigos/article.html",context)


@group_required('editores de artigos')
def new_article_view(request):

    form = ArticleForm(request.POST or None, request.FILES)
    if form.is_valid():
        new_article = form.save()
        return redirect('artigos:article_view', article_id=new_article.id)

    context = {'form': form}
    return render(request, 'artigos/newArticle.html', context)

@group_required('editores de artigos')
def edit_article_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.POST:
        form = ArticleForm(request.POST or None, request.FILES, instance=article)
        if form.is_valid():
            new_article = form.save()
            return redirect('artigos:article_view', article_id=new_article.id)
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article':article}
    return render(request, 'artigos/editArticle.html', context)

@group_required('editores de artigos')
def delete_article_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('artigos:user_view')



def user_view(request, user_id):

    user = get_object_or_404(UserProfile, id=user_id)

    context = {
        'user': user
        }

    return render(request,"artigos/user.html",context)
