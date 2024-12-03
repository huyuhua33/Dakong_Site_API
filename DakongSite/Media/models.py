# Media/models.py
# Model for storing media files
from django.db import models
import logging

logger = logging.getLogger(__name__)

class MediaFile(models.Model):
    file = models.FileField(upload_to='media/')
    upload_date = models.DateTimeField(auto_now_add=True)

logger.info("MediaFile model loaded successfully.")