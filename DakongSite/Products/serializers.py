from rest_framework import serializers
from .models import Product, ProductImage,Category

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_cover']

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent', 'children']
        extra_kwargs = {'id': {'read_only': True}}  # UUID is auto-generated

    def get_children(self, obj):
        return CategorySerializer(obj.get_children(), many=True).data

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name','category', 'description', 'price', 'stock', 'created_at', 'updated_at', 'cover_image', 'images']

    def get_cover_image(self, obj):
        cover = obj.images.filter(is_cover=True).first()
        return cover.image.url if cover else None
