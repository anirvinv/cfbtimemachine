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
    college = models.CharField(max_length=900)
    conference = models.CharField(max_length=900)

class Conference(models.Model):
    name = models.CharField(max_length=900)
    def __str__(self):
        return self.name
class College(models.Model):
    name = models.CharField(max_length=900)
    def __str__(self):
        return self.name
class Player(models.Model):
    name = models.CharField(max_length=900)
    def __str__(self):
        return self.name