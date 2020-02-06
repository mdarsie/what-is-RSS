from django.db import models

# Create your models here.


class Groups(models.Model):
    collection = models.CharField(max_length=100)

    def __str__(self):
        return self.name


