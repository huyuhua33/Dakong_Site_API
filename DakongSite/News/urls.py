# News/urls.py
# URL configuration for news related views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet



router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # CKEditor 文件上傳
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
