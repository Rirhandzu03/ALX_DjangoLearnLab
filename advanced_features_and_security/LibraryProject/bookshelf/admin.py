from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin
from .models import Book

# Register customer user model
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



