# Products/views.py
from django.views.generic import ListView, DetailView
from .models import Product,ProductImage
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer,ProductImageSerializer
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
class ProductImageViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('translations').all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]
