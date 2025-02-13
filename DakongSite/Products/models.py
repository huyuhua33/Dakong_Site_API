from django.db import models
from parler.models import TranslatableModel, TranslatedFields
import uuid
from django.utils.translation import gettext_lazy as _

class Category(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        name=models.CharField(_("Category Name"), max_length=255),
        description=models.TextField(_("Description"), blank=True, null=True)
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='subcategories',
        blank=True, null=True, verbose_name=_("Parent Category")
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name
    
# Models
class Product(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        description=models.TextField(blank=True, null=True)
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "No Name"

    def save(self, *args, **kwargs):
        # 確保至少有默認語言的翻譯
        if not self.has_translation('en'):
            self.set_current_language('en')
            self.name = "Default Name"
            self.description = "Default Description"
        super().save(*args, **kwargs)
        

class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/')
    is_cover = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # 如果沒有封面，將第一張圖片自動設為封面
        if not self.product.images.filter(is_cover=True).exists():
            self.is_cover = True
        else:
            # 如果當前圖片被設置為封面，取消其他圖片的封面狀態
            if self.is_cover:
                self.product.images.update(is_cover=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.product.safe_translation_getter('name', any_language=True) or 'Unnamed Product'}"
