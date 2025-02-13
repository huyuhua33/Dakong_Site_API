from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category

class CategoryAPITestCase(TestCase):
    def setUp(self):
        """ 初始化測試數據 """
        self.client = APIClient()
        self.parent_category = Category.objects.create(name="Parent Category", slug="parent-category")
        self.child_category = Category.objects.create(name="Child Category", slug="child-category", parent=self.parent_category)

    def test_create_category(self):
        """ 測試創建分類 """
        data = {
            "name": "New Category",
            "slug": "new-category",
            "parent": self.parent_category.id
        }
        response = self.client.post("/api/categories/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 3)

    def test_get_category_list(self):
        """ 測試獲取分類列表 """
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # 預期有2個分類

    def test_update_category(self):
        """ 測試更新分類 """
        data = {"name": "Updated Category"}
        response = self.client.patch(f"/api/categories/{self.parent_category.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.parent_category.refresh_from_db()
        self.assertEqual(self.parent_category.name, "Updated Category")

    def test_delete_category(self):
        """ 測試刪除分類 """
        response = self.client.delete(f"/api/categories/{self.child_category.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 1)

    def test_get_category_detail(self):
        """ 測試獲取單個分類詳情 """
        response = self.client.get(f"/api/categories/{self.parent_category.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Parent Category")

