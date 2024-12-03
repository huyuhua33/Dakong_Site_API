# Media/views.py
# Views for uploading media files and displaying media library
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import MediaFile
import logging

logger = logging.getLogger(__name__)

class MediaUploadView(CreateView):
    model = MediaFile
    fields = ['file']
    template_name = 'media/media_upload.html'
    success_url = '/media/library/'

logger.info("MediaUploadView loaded successfully.")

class MediaLibraryView(ListView):
    model = MediaFile
    template_name = 'media/media_library.html'
    context_object_name = 'media_files'

logger.info("MediaLibraryView loaded successfully.")