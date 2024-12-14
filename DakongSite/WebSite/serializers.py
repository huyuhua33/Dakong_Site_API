from rest_framework import serializers
# from .models import ExampleModel


# class ExampleModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExampleModel
#         fields = ['id', 'name', 'description', 'created_at']
        
from rest_framework import serializers
from .models import ToolbarItem

class ToolbarItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = ToolbarItem
        fields = ['id', 'name', 'link', 'is_visible', 'position']

    def get_name(self, obj):
        # 獲取請求中的語言代碼，默認為 'en'
        language_code = self.context.get('language_code', 'en')
        return obj.safe_translation_getter('name', language_code=language_code)

