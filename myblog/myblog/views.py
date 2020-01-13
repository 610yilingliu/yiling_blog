from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from markdown import markdown




def index(request):
    return render(request, 'index.html', context = {
        'title': 'Welcome'
    })

def en_index(request):
    articles = Article.objects.all().order_by('-create_time')
    return render(request, 'en_index.html', context = {
        'title': 'English Version : Tech Zone',
        'articles': articles,
    })

def zhcn_index(request):
    return render(request, 'index.html', context = {
        'title': '不正经的二次元杂物堆放地'
    })

def article(request, pk):
    article =get_object_or_404(Article, pk=pk)
    config = {
        'codehilite': {
            'use_pygments': False,
            'css_class': 'prettyprint linenums',
        }
    }
    article.body = markdown(article.body, extensions=['codehilite'], extension_configs=config)
    return render(request, 'en_article.html', context={
        'title': 'Article',
        'article': article
    })

    