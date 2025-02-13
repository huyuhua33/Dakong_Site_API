from django.test import TestCase
from Media.models import MediaFile

class MediaFileModelTest(TestCase):
    def setUp(self):
        self.media = MediaFile.objects.create(name="Test Image", file="test.jpg")

    def test_media_str(self):
        self.assertEqual(str(self.media), "Test Image")
