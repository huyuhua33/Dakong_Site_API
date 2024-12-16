from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import Application

class ApplicationSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Application)

    class Meta:
        model = Application
        fields = ['id', 'translations', 'created_at']



from .models import News
from .serializers import ApplicationSerializer

class NewsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=News)
    applications = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'translations', 'published_at', 'applications']