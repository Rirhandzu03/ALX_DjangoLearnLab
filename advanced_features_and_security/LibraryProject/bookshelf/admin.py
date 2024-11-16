from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

# Unregister the default Group model registration
admin.site.unregister(Group)

# Register the Group model with a custom GroupAdmin class
class CustomGroupAdmin(GroupAdmin):
    list_display = ('name',)  # Customize this as needed, like adding permissions if required
    filter_horizontal = ('permissions',)  # Allows easy selection of permissions

admin.site.register(Group, CustomGroupAdmin)

# Register CustomUser model with UserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to show in the list view
    list_filter = ('publication_year',)  # Filter by publication year
    search_fields = ('title', 'author')  # Enable search by title and author




