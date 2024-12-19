# News/views.py
# Views for listing articles and viewing article details

import logging

logger = logging.getLogger(__name__)

from rest_framework.viewsets import ModelViewSet
from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer

class NewsViewSet(ModelViewSet):
    """
    新聞的視圖集，僅返回選定語言的內容
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_serializer_context(self):
        """
        傳遞語言代碼到序列化器
        """
        context = super().get_serializer_context()
        language_code = self.request.query_params.get('languageCode', 'en')  # 默認英文
        context['language_code'] = language_code
        return context

class CommentViewSet(ModelViewSet):
    """
    新聞評論的視圖集，支持 CRUD。
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ['news']  # 按新聞過濾評論

logger.info("ArticleDetailView loaded successfully.")