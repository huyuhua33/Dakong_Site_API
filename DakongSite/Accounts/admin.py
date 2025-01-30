from django.contrib import admin
from .models import User, RoleHierarchy
from django.contrib.auth.admin import UserAdmin

# Admin Configuration
class RoleHierarchyAdmin(admin.ModelAdmin):
    list_display = ('role', 'level', 'created_by', 'description')
    search_fields = ('role', 'description')
    list_filter = ('level',)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'get_roles', 'is_staff', 'is_active')
    list_filter = ('roles', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    def get_roles(self, obj):
        return ', '.join([role.role for role in obj.roles.all()])
    get_roles.short_description = 'Roles'

admin.site.register(RoleHierarchy, RoleHierarchyAdmin)
admin.site.register(User, CustomUserAdmin)