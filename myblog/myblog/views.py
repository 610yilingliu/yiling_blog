from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    context = {}
    context['title'] = 'Welcome'
    return render(request, 'index.html', context)