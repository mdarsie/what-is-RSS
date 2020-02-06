from django.db import models

# Create your models here.


class Groups(models.Model):
    collection = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feed(models.Model):
    title = models.CharField(max_length=200)
    feed_description = models.TextField(default='')
    feed_link = models.CharField(max_length=200)
    feed_image = models.CharField(max_length=200)
    published_last = models.CharField(max_length=20)
