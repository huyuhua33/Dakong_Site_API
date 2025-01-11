from django.contrib import admin
from .models import Product,ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    inlines = [ProductImageInline]


    
admin.site.register(Product, ProductAdmin)
