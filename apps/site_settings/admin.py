from django.contrib import admin
from .models import BusinessSettings


@admin.register(BusinessSettings)
class BusinessSettingsAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'whatsapp_number', 'location_text', 'is_active', 'updated_at')
    fieldsets = (
        ('Marca', {'fields': ('business_name', 'slogan', 'logo', 'is_active')}),
        ('Home', {'fields': ('hero_title', 'hero_subtitle')}),
        ('Contacto', {'fields': ('whatsapp_number', 'instagram_url', 'location_text', 'delivery_notes')}),
    )

    def has_add_permission(self, request):
        return not BusinessSettings.objects.exists()
