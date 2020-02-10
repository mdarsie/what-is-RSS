from rest_framework import serializers
from .models import Group, Feed, Article

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'


class FeedSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Feed
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'


class MegaSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    feeds = FeedSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('article_link', 'article_title', 'feed_title', 'group', 'collection')