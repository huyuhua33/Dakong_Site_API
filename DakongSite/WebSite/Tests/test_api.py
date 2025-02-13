from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from WebSite.models import Page

class PageAPITest(APITestCase):
    def setUp(self):
        self.page = Page.objects.create(title="Test API Page", slug="test-api", content="API Content")

    def test_get_page_list(self):
        url = reverse("website-api:page-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_page(self):
        url = reverse("website-api:page-list")
        data = {"title": "New Page", "slug": "new-page", "content": "New content"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
