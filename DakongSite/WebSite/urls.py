# WebSite/urls.py
from django.urls import path,include
from . import views
import logging
from django.conf import settings
from rest_framework.routers import DefaultRouter


logger = logging.getLogger(__name__)

router = DefaultRouter()
router.register(r'toolbar-items', views.ToolbarItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# from django.urls import path
# from . import views



# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


logger.info("WebSite URLs configured successfully.")