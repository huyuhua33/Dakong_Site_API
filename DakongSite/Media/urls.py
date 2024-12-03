# Media/urls.py
# URL configuration for media related views
from django.urls import path
from . import views
import logging

logger = logging.getLogger(__name__)

urlpatterns = [
    path('upload/', views.MediaUploadView.as_view(), name='media_upload'),
    path('library/', views.MediaLibraryView.as_view(), name='media_library'),
]

logger.info("Media URLs configured successfully.")
