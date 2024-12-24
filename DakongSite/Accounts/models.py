# # Account App

from django.contrib.auth.models import AbstractUser
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
import logging

logger = logging.getLogger(__name__)



class User(AbstractUser, TranslatableModel):
    """
    自定義用戶模型，支持多語言姓名。
    """
    translations = TranslatedFields(
        display_name=models.CharField(max_length=255, blank=True, null=True),  # 用戶顯示名稱
    )
    role = models.CharField(
        max_length=50,
        choices=[
            ('user', 'User'),
            ('admin', 'Admin'),
            ('guest', 'Guest'),
        ],
        default='user',
    )
    phone = models.CharField(max_length=15, blank=True, null=True)  # 電話號碼
    address = models.TextField(blank=True, null=True)  # 用戶地址

    def __str__(self):
        return self.safe_translation_getter('display_name', default=self.username)


logger.info("CustomUser model loaded successfully.")
