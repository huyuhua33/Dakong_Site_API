from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class AccountAPITest(APITestCase):
    def test_register_user(self):
        url = reverse("account-api:register")
        data = {"username": "newuser", "email": "new@example.com", "password": "securepass"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
