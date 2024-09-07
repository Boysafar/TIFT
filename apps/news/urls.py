from django.urls import path
from .views import NewsDetailView, NewsListView

urlpatterns = [
    path('news/', NewsListView.as_view(), name="news_list"),
    path('news/<slug:slug>/', NewsDetailView.as_view()),
]
