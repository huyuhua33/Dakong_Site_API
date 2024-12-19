from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import News

@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('translations__title',)
    list_filter = ('published_at',)

    # 選擇性展示相關評論，僅供參考
    def comments_count(self, obj):
        return obj.comments.count()
    comments_count.short_description = 'Comments Count'
