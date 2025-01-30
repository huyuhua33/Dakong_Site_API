# Products/models.py
from parler.models import TranslatableModel, TranslatedFields
from django.db import models
import uuid
from parler.models import TranslatableModel, TranslatedFields

class Product(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        description=models.TextField(blank=True, null=True)
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
    
class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/')
    is_cover = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Automatically set the first uploaded image as the cover if no other cover exists
        if not self.product.images.filter(is_cover=True).exists():
            self.is_cover = True
        else:
            # If this image is marked as cover, reset others
            if self.is_cover:
                self.product.images.update(is_cover=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.product.name}"