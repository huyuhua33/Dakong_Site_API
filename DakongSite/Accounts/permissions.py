from rest_framework.permissions import BasePermission
from rest_framework import serializers, status
from rest_framework.response import Response  # Add this import
from functools import wraps


class IsAdminUser(BasePermission):
    """
    僅允許管理員用戶訪問
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

# Decorators
def role_required(required_role):
    """Decorator to check if the user has the required role or higher"""
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)
            if not request.user.has_permission_level(required_role):
                return Response({"detail": f"Permission denied. Minimum role '{required_role}' required."}, status=status.HTTP_403_FORBIDDEN)
            return view_func(self, request, *args, **kwargs)
        return _wrapped_view
    return decorator
