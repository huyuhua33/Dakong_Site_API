from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from .models import News

class NewsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=News)

    class Meta:
        model = News
        fields = ['id', 'translations', 'published_at']
        