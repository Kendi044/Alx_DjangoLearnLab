from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

class CustomUserAdmin(UserAdmin):
    """
    Custom Admin interface for the CustomUser model.
    """
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
