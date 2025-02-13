from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from News.models import Article

class NewsAPITest(APITestCase):
    def setUp(self):
        self.article = Article.objects.create(title="Breaking News", content="This is news content.")

    def test_get_news_list(self):
        url = reverse("news-api:article-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
