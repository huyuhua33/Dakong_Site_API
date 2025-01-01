from rest_framework import serializers
from .models import RoleHierarchy,User

# Serializers
class RoleHierarchySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleHierarchy
        fields = ['id', 'role', 'level']

class UserSerializer(serializers.ModelSerializer):
    role_display = serializers.SerializerMethodField()
    role_ids = serializers.PrimaryKeyRelatedField(queryset=RoleHierarchy.objects.all(), many=True, source='roles')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role_ids', 'role_display', 'phone', 'address']

    def get_role_display(self, obj):
        return ', '.join([role.role for role in obj.roles.all()])

class UserDetailSerializer(serializers.ModelSerializer):
    role_ids = serializers.PrimaryKeyRelatedField(queryset=RoleHierarchy.objects.all(), many=True, source='roles')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role_ids', 'phone', 'address', 'date_joined', 'last_login']