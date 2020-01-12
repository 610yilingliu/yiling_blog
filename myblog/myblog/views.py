from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import markdown



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