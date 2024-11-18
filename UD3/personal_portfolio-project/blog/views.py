from django.shortcuts import render
from .models import Article

def all_blogs(request):
    articles = Article.objects.order_by('-date')[:3]
    return render(request, 'blog/all_blogs.html', {'articles':articles})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/detail.html', {'id': article_id})