from django.db import models

# Create your models here.
from django.db.models import CharField


class Groups(models.Model):
    collection = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feed(models.Model):
    feed_title = models.CharField(max_length=200)
    feed_description = models.TextField(default='')
    feed_link = models.CharField(max_length=200)
    feed_image = models.CharField(max_length=200)
    feed_last_published = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_description = models.TextField(default='')
    article_link = models.CharField(max_length=200)
    article_image = models.CharField(max_length=200)
    article_last_published = models.CharField(max_length=20)

    def __str__(self):
        return self.name
