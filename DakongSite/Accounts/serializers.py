from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'display_name', 'role', 'phone', 'address']

    def get_display_name(self, obj):
        language_code = self.context.get('language_code', 'en')
        return obj.safe_translation_getter('display_name', language_code=language_code)
