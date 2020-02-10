from rest_framework import serializers
from .models import Group, Feed, Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'feed', 'article_title', 'article_link', 'article_description', 'article_published', 'article_guid')


class FeedSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Feed
        fields = ('id', 'group', 'feed_title', 'feed_description', 'feed_link', 'article_title')


class GroupSerializer(serializers.ModelSerializer):
    feeds = FeedSerializer(many=True, read_only=True)
    
    class Meta:
        model = Group
        fields = ('collection', 'feed_title')