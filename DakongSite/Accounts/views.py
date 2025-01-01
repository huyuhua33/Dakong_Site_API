
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.cache import cache
from .userRole import RoleChoices
from .models import RoleHierarchy,User
from .serializers import UserSerializer,RoleHierarchySerializer,UserDetailSerializer

# Views
class RoleHierarchyViewSet(ModelViewSet):
    queryset = RoleHierarchy.objects.all()
    serializer_class = RoleHierarchySerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(ModelViewSet):
    queryset = User.objects.prefetch_related('roles').all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)

    def get_admin_role(self):
        """Cache the admin role to avoid repetitive database queries"""
        admin_role = cache.get('admin_role')
        if not admin_role:
            admin_role = RoleHierarchy.objects.get(role=RoleChoices.ADMIN)
            cache.set('admin_role', admin_role, timeout=3600)  # Cache for 1 hour
        return admin_role

    # 這個錯誤是因為 @action 裝飾器被用在了 list 方法，而 list 方法是 Django Rest Framework 預設的路由之一，這會導致路由衝突。
    # @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
