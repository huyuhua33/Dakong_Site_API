# WebSite/urls.py
from django.urls import path
from . import views
import logging

logger = logging.getLogger(__name__)

urlpatterns = [
    path('', views.homepage, name='home'),
]

# from django.urls import path
# from . import views

urlpatterns = [
    path('api/language/<str:lang_code>/', views.get_language_content, name='get_language_content'),
]


logger.info("WebSite URLs configured successfully.")