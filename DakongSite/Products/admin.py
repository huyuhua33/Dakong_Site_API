from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')
    search_fields = ('translations__name', 'translations__description')
    list_filter = ('created_at', 'updated_at')
    inlines = [ProductImageInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:  # 在編輯模式下禁用非編輯欄位
            return ['created_at', 'updated_at']
        return []

admin.site.register(Product, ProductAdmin)
