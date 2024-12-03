# Account/views.py
# Sign up view for new users
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
import logging

logger = logging.getLogger(__name__)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

logger.info("SignUpView loaded successfully.")