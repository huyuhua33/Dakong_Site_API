# WebSite/urls.py
from django.urls import path
from .views import ProductViewSet,ProductImageViewSet
import logging
from rest_framework.routers import DefaultRouter
from django.urls import path, include

logger = logging.getLogger(__name__)
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'product-images', ProductImageViewSet, basename='productimage')

urlpatterns = [
    path('', include(router.urls)),
]


logger.info("WebSite URLs configured successfully.")