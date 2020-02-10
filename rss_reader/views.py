from rest_framework import viewsets

from .serializers import GroupSerializer, FeedSerializer, ArticleSerializer, MegaSerializer
from .models import Group, Feed, Article

class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FeedView(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class MegaView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class= MegaSerializer


