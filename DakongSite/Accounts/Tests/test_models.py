from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username="testuser", email="test@example.com", password="securepass")
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.username, "testuser")
