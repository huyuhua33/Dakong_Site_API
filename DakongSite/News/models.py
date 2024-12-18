from parler.models import TranslatableModel, TranslatedFields
from django.db import models
import logging

logger = logging.getLogger(__name__)

from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# class Application(TranslatableModel):
#     """
#     Represents an application or feature associated with news.
#     """
#     translations = TranslatedFields(
#         name=models.CharField(max_length=100),  # Application name (multilingual)
#         description=models.TextField(blank=True),  # Application description
#     )
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.safe_translation_getter('name', any_language=True)

from ckeditor.fields import RichTextField

class News(TranslatableModel):
    """
    新聞模型，支持富文本編輯。
    """
    translations = TranslatedFields(
        title=models.CharField(max_length=255),  # 新聞標題
        content=RichTextField(),  # 使用 CKEditor 的富文本字段
    )
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # 圖片字段
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)
logger.info("Article model loaded successfully.")