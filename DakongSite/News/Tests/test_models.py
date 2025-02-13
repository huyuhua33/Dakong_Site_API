from django.test import TestCase
from News.models import Article

class ArticleModelTest(TestCase):
    def setUp(self):
        self.article = Article.objects.create(title="Test News", content="This is a test news.")

    def test_article_str(self):
        self.assertEqual(str(self.article), "Test News")
