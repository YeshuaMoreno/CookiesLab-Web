from django.contrib import admin
from django.utils.html import format_html
from .models import CustomerOrder, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('subtotal',)
    autocomplete_fields = ('product',)

    @admin.display(description='Subtotal')
    def subtotal(self, obj):
        return f'${obj.subtotal:.2f}' if obj.pk else '—'


@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone', 'delivery_place', 'payment_method', 'status', 'total_display', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('customer_name', 'phone', 'delivery_place', 'notes')
    list_editable = ('status',)
    readonly_fields = ('total_display', 'whatsapp_link', 'created_at', 'updated_at')
    inlines = [OrderItemInline]
    fieldsets = (
        ('Cliente', {'fields': ('customer_name', 'phone')}),
        ('Entrega', {'fields': ('delivery_place', 'delivery_datetime', 'payment_method')}),
        ('Estado', {'fields': ('status', 'notes')}),
        ('Totales', {'fields': ('total_display',)}),
        ('Canal', {'fields': ('whatsapp_link', 'whatsapp_message'), 'classes': ('collapse',)}),
        ('Registro', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )

    @admin.display(description='Total')
    def total_display(self, obj):
        return f'${obj.total:.2f}' if obj.pk else '—'

    @admin.display(description='Abrir en WhatsApp')
    def whatsapp_link(self, obj):
        if obj.phone:
            num = obj.phone.replace('+', '').replace(' ', '').replace('-', '')
            return format_html(
                '<a href="https://wa.me/{}" target="_blank" rel="noopener">Contactar por WhatsApp ↗</a>',
                num,
            )
        return '—'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price', 'subtotal_display')
    search_fields = ('order__customer_name', 'product__name')
    autocomplete_fields = ('product',)

    @admin.display(description='Subtotal')
    def subtotal_display(self, obj):
        return f'${obj.subtotal:.2f}'
