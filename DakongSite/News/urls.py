# News/urls.py
# URL configuration for news related views
from django.urls import path
from . import views
import logging

logger = logging.getLogger(__name__)

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
]

logger.info("News URLs configured successfully.")