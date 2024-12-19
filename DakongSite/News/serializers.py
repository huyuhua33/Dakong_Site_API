from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import News, Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    評論序列化器
    """
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at']

class NewsSerializer(serializers.ModelSerializer):
    """
    僅返回選定語言的新聞序列化器
    """
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'published_at', 'image']

    def get_title(self, obj):
        """
        根據語言代碼返回標題
        """
        language_code = self.context.get('language_code', 'en')
        return obj.safe_translation_getter('title', language_code=language_code)

    def get_content(self, obj):
        """
        根據語言代碼返回內容
        """
        language_code = self.context.get('language_code', 'en')
        return obj.safe_translation_getter('content', language_code=language_code)