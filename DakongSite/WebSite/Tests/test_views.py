from django.test import TestCase
from django.urls import reverse
from WebSite.models import Page

class PageViewTest(TestCase):
    def setUp(self):
        self.page = Page.objects.create(title="Test Page", slug="test-page", content="Hello World")

    def test_page_detail_view(self):
        response = self.client.get(reverse("website:page_detail", args=[self.page.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Page")
