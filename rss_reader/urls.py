from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('group', views.GroupView)
router.register('feed', views.FeedView)
router.register('article', views.ArticleView)

urlpatterns = [path('', include(router.urls))]
