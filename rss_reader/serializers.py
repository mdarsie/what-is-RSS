from rest_framework import serializers
from .models import Group, Feed, Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'feed', 'article_title', 'article_link', 'article_description', 'article_published', 'article_guid')


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'group', 'feed_title', 'feed_description', 'feed_link', 'article_title')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('collection', 'feed_title')