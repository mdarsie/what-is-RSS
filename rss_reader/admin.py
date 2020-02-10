from django.contrib import admin

# Register your models here.
from .models import Group, Feed, Article

admin.site.register({Group, Feed, Article})
