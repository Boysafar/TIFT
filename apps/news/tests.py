# tests.py
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import News
from datetime import datetime


class NewsContentAPITestCase(APITestCase):
    def setUp(self):
        self.item_active = News.objects.create(
            title="test news",
            body="test news test",
            is_published=False,
            publish_time=datetime(2024, 8, 29, 12, 30, 30),
        )
        self.item_inactive = News.objects.create(
            title="test news",
            body="test news test",
            is_published=False,
            publish_time=datetime(2024, 8, 29, 12, 30, 30),
        )
        self.list_url = reverse("news_list")

    def test_news_content_list_api(self):
        response = self.client.get(self.list_url)
        r = response.json()
        count = r.get('count')
        results = r.get('results', [])
        if results:
            data = results[0]
            self.assertEqual(response.status_code, 200)
            self.assertEqual(1, count)
            self.assertEqual(self.item_active.title, data['title'])
        else:
            self.fail("Results list is empty.")


