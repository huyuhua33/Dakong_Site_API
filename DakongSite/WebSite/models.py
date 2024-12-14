# WebSite/models.py
from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# HomePageContent model to store homepage information
# WebSite/models.py
from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class HomePageContent(TranslatableModel):
    translations = TranslatedFields(
        headline=models.CharField(max_length=200),  # Title of the homepage section
        subheadline=models.TextField(),  # Subtitle or detailed description
        headline=models.CharField(max_length=200),  # Title of the homepage section
        subheadline=models.TextField(),  # Subtitle or detailed description
    )
    promotional_image = models.ImageField(upload_to='homepage/')  # Image for promotional purposes  # Image for promotional purposes

    def __str__(self):
        return self.safe_translation_getter('headline', any_language=True)

class PageContent(TranslatableModel):
    slug = models.SlugField(unique=True)
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=models.TextField()
    )

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

class MediaFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')  # For any file type
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ToolbarItem(TranslatableModel):
    
    translations = TranslatedFields(
        name=models.CharField(max_length=100),  # 多語顯示名稱
    )
    link = models.CharField(max_length=255)  # 鏈接地址
    is_visible = models.BooleanField(default=True)  # 是否顯示
    position = models.PositiveIntegerField(default=0,unique=True)  # 順序排序

    def save(self, *args, **kwargs):
        if self.position is None:
            # 自動設置 position 為當前最大值 + 1
            max_position = ToolbarItem.objects.aggregate(models.Max('position'))['position__max'] or 0
            self.position = max_position + 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
