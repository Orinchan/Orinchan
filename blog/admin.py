from django import forms
from django.contrib import admin
from .models import Post, Contact

# Register your models here.


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 18,
                    'style': 'font-family: inherit;',
                }
            ),
        }
        help_texts = {
            'description': (
                'Usa líneas en blanco para separar párrafos. '
                'El sitio respetará esos saltos de línea.'
            ),
        }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'read')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('read', 'created_at')
    readonly_fields = ('created_at',)
