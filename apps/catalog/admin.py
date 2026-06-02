from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('thumb', 'name', 'category', 'price', 'status', 'is_featured', 'updated_at')
    list_editable = ('price', 'status', 'is_featured')
    list_filter = ('status', 'is_featured', 'category')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('thumb_large', 'created_at', 'updated_at')
    autocomplete_fields = ('category',)
    fieldsets = (
        ('Información', {'fields': ('name', 'slug', 'category', 'description')}),
        ('Imagen', {'fields': ('image', 'thumb_large')}),
        ('Precio y estado', {'fields': ('price', 'status', 'is_featured')}),
        ('Registro', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )

    @admin.display(description='Foto')
    def thumb(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:48px;width:48px;object-fit:cover;border-radius:8px;">',
                obj.image.url,
            )
        return '🍪'

    @admin.display(description='Vista previa')
    def thumb_large(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:200px;border-radius:12px;">',
                obj.image.url,
            )
        return 'Sin imagen'
