
from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import ToolbarItem

class ToolbarItemSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=ToolbarItem)

    class Meta:
        model = ToolbarItem
        fields = ['id', 'translations', 'link', 'is_visible', 'position']
