from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)

class Tag(models.Model):
    name = models.CharField(max_length = 50)

class Language(models.Model):
    is_en = models.BooleanField()

class Article(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    time = models.DateTimeField()
    tags = models.ManyToManyField(Tag, blank = True)
    summary = models.CharField(max_length = 300, blank = True)
    ## if no CASCADE, there will be an error while migrating database.
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    language = models.ForeignKey(Language, on_delete = models.CASCADE)