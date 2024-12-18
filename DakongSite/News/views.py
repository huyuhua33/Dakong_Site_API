# News/views.py
# Views for listing articles and viewing article details
from django.views.generic import ListView, DetailView

import logging

logger = logging.getLogger(__name__)

from rest_framework.viewsets import ModelViewSet
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all().order_by('-published_at')
    serializer_class = NewsSerializer


logger.info("ArticleDetailView loaded successfully.")