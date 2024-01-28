"""
Django admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin interface for user."""
    ordering = ['id']
    list_display = ['username', 'email']
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        (
            _('permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets =(
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'email',
                'is_staff',
                'is_superuser',
                'is_active',
            )
        }),
    )

admin.site.register(models.User, UserAdmin)
admin.site.register(models.CommunityPost)
