# Account/forms.py
# Custom user creation form to register new users
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
import logging

logger = logging.getLogger(__name__)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address')

logger.info("CustomUserCreationForm loaded successfully.")
