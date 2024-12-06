from django.contrib import admin

# Register your models here.
from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import PageContent

@admin.register(PageContent)
class PageContentAdmin(TranslatableAdmin):
    list_display = ('slug', 'title')
