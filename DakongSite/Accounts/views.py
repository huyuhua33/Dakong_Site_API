# Account/views.py
# Sign up view for new users
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
import logging

logger = logging.getLogger(__name__)

from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self):
        """
        傳遞語言代碼到序列化器
        """
        context = super().get_serializer_context()
        language_code = self.request.query_params.get('languageCode', 'en')  # 默認英文
        context['language_code'] = language_code
        return context


logger.info("SignUpView loaded successfully.")