"""
Django admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin interface for user."""
    ordering = ['id']
    list_display = ['username', 'email']

admin.site.register(models.User, UserAdmin)
