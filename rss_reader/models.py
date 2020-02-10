from django.db import models

# Create your models here.
from django.db.models import CharField


class Group(models.Model):
    collection = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.collection


class Feed(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='Feed')
    feed_title = models.CharField(max_length=200)
    feed_description = models.TextField(default='')
    feed_link = models.CharField(max_length=200)

    def __str__(self):
        return self.feed_title


class Article(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='Article')
    article_title = models.CharField(max_length=200)
    article_link = models.CharField(max_length=200)
    article_description = models.TextField(default='')
    article_published = models.DateTimeField(null=True, blank=True)
    article_guid = models.TextField(max_length=200)

    def __str__(self):
        return self.article_title
