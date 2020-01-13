from django.contrib import admin
from .models import *
 
# view for articles in admin control panel
class ArticleAdminView(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modify_time', 'category', 'language']

admin.site.register(Article, ArticleAdminView)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Language)