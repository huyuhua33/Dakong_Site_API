from parler.models import TranslatableModel, TranslatedFields
from django.db import models
import logging

logger = logging.getLogger(__name__)

class Article(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        content=models.TextField()
    )
    published_date = models.DateTimeField(auto_now_add=True)

logger.info("Article model loaded successfully.")