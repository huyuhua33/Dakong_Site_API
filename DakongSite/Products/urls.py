# WebSite/urls.py
from django.urls import path
from . import views
import logging

logger = logging.getLogger(__name__)


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]


logger.info("WebSite URLs configured successfully.")