from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    # if the article is a youtube link, then the image field is the date :/ lazy
    img = models.CharField(max_length=900)
    iframe = models.CharField(max_length=2)
