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
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class News(TranslatableModel):
    """
    新聞模型，支持富文本編輯和圖片上傳。
    """
    translations = TranslatedFields(
        title=models.CharField(max_length=255),  # 新聞標題
        content=RichTextUploadingField(),  # 使用 CKEditor 的富文本字段，支持圖片上傳
    )
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # 新聞附加圖片

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

class Comment(models.Model):
    """
    新聞評論模型。
    """
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)  # 關聯的新聞
    author = models.CharField(max_length=100)  # 評論作者
    content = models.TextField()  # 評論內容
    created_at = models.DateTimeField(auto_now_add=True)  # 評論創建時間

    def __str__(self):
        return f"Comment by {self.author} on {self.news}"

logger.info("Article model loaded successfully.")