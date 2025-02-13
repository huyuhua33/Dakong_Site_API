# News/urls.py
# URL configuration for news related views
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet



router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ckeditor5/', include('django_ckeditor_5.urls')),  # CKEditor 文件上傳
]