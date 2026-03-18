from django.contrib import admin
from .models import Post, Contact

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'read')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('read', 'created_at')
    readonly_fields = ('created_at',)