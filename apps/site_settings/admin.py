from django.contrib import admin
from django.utils.html import format_html
from .models import BusinessSettings


@admin.register(BusinessSettings)
class BusinessSettingsAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'whatsapp_number', 'instagram_url', 'location_text', 'is_active', 'updated_at')
    readonly_fields = ('logo_preview', 'updated_at')
    fieldsets = (
        ('Marca', {'fields': ('business_name', 'slogan', 'logo', 'logo_preview', 'is_active')}),
        ('Portada (Home)', {'fields': ('hero_title', 'hero_subtitle')}),
        ('Contacto', {'fields': ('whatsapp_number', 'instagram_url', 'location_text')}),
        ('Entregas', {'fields': ('delivery_notes',)}),
        ('Registro', {'fields': ('updated_at',), 'classes': ('collapse',)}),
    )

    @admin.display(description='Vista previa del logo')
    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-height:100px;border-radius:10px;">',
                obj.logo.url,
            )
        return 'Sin logo — se mostrará el emoji 🍪'

    def has_add_permission(self, request):
        return not BusinessSettings.objects.exists()
