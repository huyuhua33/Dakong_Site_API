from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Product, ProductImage,Category

# admin.py
class CategoryAdmin(TranslatableAdmin):
    list_display = ('id', 'name', 'slug', 'parent')
    search_fields = ('translations__name', 'translations__slug')
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'parent')}),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}  # 讓 Django Admin 自動填充 slug

admin.site.register(Category, CategoryAdmin)




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


# # 內聯管理翻譯
# class CategoryTranslationInline(TranslatableTabularInline):
#     model = Category._meta.get_field('translations').remote_field.model
#     fields = ("name", "description")

# # 註冊 Category 模型到 Django Admin
# @admin.register(Category)
# class CategoryAdmin(TranslatableAdmin, MPTTModelAdmin):
#     list_display = ("get_translated_name", "parent", "slug", "id")  # 確保名稱可翻譯顯示
#     list_filter = ("parent",)
#     search_fields = ("translations__name", "slug")  # 正確的搜尋方式
#     ordering = ["tree_id", "lft"]

#     inlines = [CategoryTranslationInline]  # 內聯翻譯

#     fieldsets = (
#         (None, {
#             "fields": ("slug", "parent"),
#         }),
#         ("Advanced options", {
#             "classes": ("collapse",),
#             "fields": ("description",),
#         }),
#     )

#     def get_translated_name(self, obj):
#         """ 確保 Django-Parler 正確處理翻譯 """
#         return obj.safe_translation_getter("name", any_language=True) or "Unnamed Category"
#     get_translated_name.admin_order_field = "translations__name"
#     get_translated_name.short_description = "Category Name"

#     @admin.display(description="Category Name")
#     def name(self, obj):
#         """ 取得翻譯名稱 """
#         return obj.safe_translation_getter("name", any_language=True) or "Unnamed Category"

#     def get_queryset(self, request):
#         """ 確保預先載入翻譯，提高效能 """
#         return super().get_queryset(request).prefetch_related("translations")