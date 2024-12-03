# Products/models.py
from parler.models import TranslatableModel, TranslatedFields
from django.db import models

class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200),  # Name of the product
        description=models.TextField()  # Description of the product
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
