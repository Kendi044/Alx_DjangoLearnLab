from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Defines the custom admin for the CustomUser model.
    This includes displaying custom fields in the admin interface.
    """
    
    # Fields to be displayed in the list view of the admin
    list_display = UserAdmin.list_display + ('date_of_birth', 'profile_photo')
    
    # Fieldsets for the change user form in the admin
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # Fieldsets for the add user form in the admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
# Register the custom user model and its admin class
admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
