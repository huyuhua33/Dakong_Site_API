
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet,RoleHierarchyViewSet
import logging

logger = logging.getLogger(__name__)

# URLs

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'roles', RoleHierarchyViewSet, basename='role')

urlpatterns = [
    path('', include(router.urls)),
]

logger.info("Account URLs configured successfully.")