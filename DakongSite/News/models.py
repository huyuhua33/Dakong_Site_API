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

class News(TranslatableModel):
    """
    News model, linked to applications or features.
    """
    translations = TranslatedFields(
        title=models.CharField(max_length=255),  # News title
        content=models.TextField(),  # News content
    )
    published_at = models.DateTimeField(auto_now_add=True)
    # applications = models.ManyToManyField(Application, related_name="news", blank=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

logger.info("Article model loaded successfully.")