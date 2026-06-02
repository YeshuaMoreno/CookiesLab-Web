from django.contrib import admin
from django.utils.html import format_html
from .models import Promotion


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'is_current_display', 'starts_at', 'ends_at', 'created_at')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    readonly_fields = ('image_preview', 'is_current_display')

    @admin.display(boolean=True, description='Activa ahora')
    def is_current_display(self, obj):
        return obj.is_current

    @admin.display(description='Vista previa')
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:160px;border-radius:12px;">',
                obj.image.url,
            )
        return 'Sin imagen'
