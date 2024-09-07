from rest_framework import generics
from apps.news.models import News
from apps.news.serializer import NewsListSerializer, NewsDetailSerializer
from apps.news.pagination import CustomNewsPagination
from django.utils import timezone


class NewsListView(generics.ListAPIView):
    queryset = News.objects.filter(
        is_published=True,
        publish_time__lte=timezone.now(),
    ).order_by('-id')
    serializer_class = NewsListSerializer
    pagination_class = CustomNewsPagination


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.filter(
        is_published=True,
        publish_time__lte=timezone.now(),
    ).order_by('-id')
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'
