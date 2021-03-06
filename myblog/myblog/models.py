from django.db import models
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length = 100,unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 50,unique=True)
    
    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length = 10,unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 100,unique=True)
    body = models.TextField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    summary = models.CharField(max_length = 300, blank = True)
    ## if no CASCADE, there will be an error while migrating database.
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    language = models.ForeignKey(Language, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myblog:article', kwargs={'pk': self.pk})
