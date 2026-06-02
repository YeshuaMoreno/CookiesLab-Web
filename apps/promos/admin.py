from django.contrib import admin
from .models import Promotion


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'starts_at', 'ends_at', 'created_at')
    list_filter = ('is_active', 'starts_at', 'ends_at')
    search_fields = ('title', 'description')
