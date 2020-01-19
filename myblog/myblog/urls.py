"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'myblog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('zhcn_index/', views.zhcn_index, name ='zhcn_index'),
    path('en_index/', views.en_index, name = 'en_index'),
    path('article_en/<int:pk>/', views.article, name='article'),
    path('en_tags/<int:pk>/', views.en_tags, name='en_tags'),
    path('en_categories/<int:pk>/', views.en_categories, name='en_categories'),
]
