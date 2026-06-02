from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'status', 'is_featured', 'updated_at')
    list_editable = ('price', 'status', 'is_featured')
    list_filter = ('status', 'is_featured', 'category')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ('category',)
