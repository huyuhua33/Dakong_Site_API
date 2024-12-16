from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import News

# @admin.register(Application)
# class ApplicationAdmin(TranslatableAdmin):
#     list_display = ('name', 'created_at')

@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    list_display = ('title', 'published_at')
    # filter_horizontal = ('applications',)  # Enable multi-select for applications
