from django.test import TestCase
from website.models import Page

class PageModelTest(TestCase):
    def setUp(self):
        self.page = Page.objects.create(title="Test Page", slug="test-page", content="Hello World")

    def test_create_page(self):
        self.assertEqual(Page.objects.count(), 1)

    def test_page_str(self):
        self.assertEqual(str(self.page), "Test Page")

    def test_page_absolute_url(self):
        self.assertEqual(self.page.get_absolute_url(), f"/page/{self.page.slug}/")
