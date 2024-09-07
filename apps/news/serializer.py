from rest_framework import serializers
from .models import News
from django.utils.text import slugify


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'slug', 'publish_time',)


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'body', 'is_published', 'publish_time', 'created_at', 'slug']