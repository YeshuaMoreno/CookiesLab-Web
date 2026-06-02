from django.contrib import admin
from .models import CustomerOrder, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    autocomplete_fields = ('product',)


@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone', 'delivery_place', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'phone', 'delivery_place', 'notes')
    list_editable = ('status',)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price')
    search_fields = ('order__customer_name', 'product__name')
    autocomplete_fields = ('order', 'product')
