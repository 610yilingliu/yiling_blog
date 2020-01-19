from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from markdown import markdown
from .models import *


def tag_list_en(request):
    '''
    tag list in template
    '''
    tg = Tag.objects.all()
    return tg

def cat_list_en(request):
    '''
    Categort list in template
    '''
    cats = Category.objects.all()
    return cats

def index(request):
    return render(request, 'index.html', context={
        'title': 'Welcome'
    })

def en_index(request):
    articles = Article.objects.all().order_by('-create_time')
    return render(request, 'en_index.html', context={
        'title': 'English Version : Tech Zone',
        'articles': articles,
        'tgs' : tag_list_en(request),
        'cats' :cat_list_en(request)
    })

def zhcn_index(request):
    return render(request, 'zhcn_index.html', context={
        'title': '不正经的二次元杂物堆放地'
    })

def article(request, pk):
    current_article = get_object_or_404(Article, pk=pk)
    # config = {
    #     'codehilite': {
    #         'use_pygments': True,
    #         'css_class': 'prettyprint linenums'
    #     }
    # }
    # article.body = markdown(article.body, extensions=['codehilite'], extension_configs=config)
    current_article.body = markdown(current_article.body)
    return render(request, 'en_article.html', context={
        'title': 'Articles',
        'article': current_article,
        'tgs' : tag_list_en(request),
        'cats' :cat_list_en(request)
    })

def en_tags(request, pk):
    article_objs = Article.objects.filter(tags__pk=pk, language__name="English").order_by('-create_time')
    current_tag = Tag.objects.filter(pk=pk).first().name
    return render(request, 'en_tag.html', context={
        'title': 'Tag ' + current_tag,
        'tag_name': current_tag,
        'articles' : article_objs,
        'tgs' : tag_list_en(request),
        'cats' :cat_list_en(request)
    })
    
def en_categories(request, pk):
    article_objs = Article.objects.filter(category__pk=pk, language__name="English").order_by('-create_time')
    current_cat = Category.objects.filter(pk=pk).first().name
    return render(request, 'en_category.html', context={
        'title': 'Category ' + current_cat,
        'cat_name': current_cat,
        'articles' : article_objs,
        'tgs' : tag_list_en(request),
        'cats' :cat_list_en(request)
    })

