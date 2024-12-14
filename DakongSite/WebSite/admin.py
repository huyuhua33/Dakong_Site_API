from django.contrib import admin
from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import ToolbarItem
# Register your models here.
from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import PageContent,MediaFile

@admin.register(PageContent)
class PageContentAdmin(TranslatableAdmin):
    list_display = ('slug', 'title')

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'description')
    search_fields = ('name',)
    list_filter = ('name',)  # Adds a filter sidebar
    ordering = ('name',)     # Orders by name
    fieldsets = (
        (None, {
            'fields': ('name', 'file', 'description'),
        }),
    )
    

@admin.register(ToolbarItem)
class ToolbarItemAdmin(TranslatableAdmin):
    list_display = ('name', 'link', 'is_visible', 'position')  # 顯示列表中的字段
    list_editable = ('is_visible', 'position')  # 可直接在列表中編輯
    ordering = ('position',)  # 按 position 排序
    search_fields = ('translations__name',)  # 支持多語搜索
    
    # def save_model(self, request, obj, form, change):
    #     # 自動處理 position 的唯一性
    #     if not obj.position:
    #         max_position = ToolbarItem.objects.aggregate(model.Max('position'))['position__max'] or 0
    #         obj.position = max_position + 1
    #     super().save_model(request, obj, form, change)