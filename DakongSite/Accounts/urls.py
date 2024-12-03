# Account/urls.py
# URL configuration for account related views (login, logout, signup)
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
import logging

logger = logging.getLogger(__name__)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]

logger.info("Account URLs configured successfully.")