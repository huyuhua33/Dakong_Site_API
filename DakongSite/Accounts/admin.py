from django.contrib import admin
from .models import User, RoleHierarchy
from django.contrib.auth.admin import UserAdmin

# Admin Configuration
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'get_roles', 'is_staff', 'is_active')
    list_filter = ('roles', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'phone', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'roles')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'roles')}
        ),
    )

    def get_roles(self, obj):
        """Display user roles"""
        return ', '.join([role.role for role in obj.roles.all()])
    get_roles.short_description = 'Roles'


admin.site.register(User, CustomUserAdmin)
admin.site.register(RoleHierarchy)