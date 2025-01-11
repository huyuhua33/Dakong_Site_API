from rest_framework import serializers
from .models import Product,ProductImage


from rest_framework import serializers


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_cover']
        
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'cover_image', 'images', 'created_at', 'updated_at']

    def get_cover_image(self, obj):
        cover_image = obj.images.filter(is_cover=True).first()
        return cover_image.image.url if cover_image else None
