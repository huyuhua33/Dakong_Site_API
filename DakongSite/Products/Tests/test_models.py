from django.test import TestCase
from Products.models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Laptop", price=1000)

    def test_product_str(self):
        self.assertEqual(str(self.product), "Laptop")
