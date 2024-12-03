# WebSite/urls.py
from django.urls import path
from . import views
import logging

logger = logging.getLogger(__name__)

urlpatterns = [
    path('', views.homepage, name='home'),
]

logger.info("WebSite URLs configured successfully.")