from django.db import models
from apps.catalog.models import Product


class CustomerOrder(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pendiente'
        CONFIRMED = 'confirmed', 'Confirmado'
        DELIVERED = 'delivered', 'Entregado'
        CANCELLED = 'cancelled', 'Cancelado'

    class PaymentMethod(models.TextChoices):
        CASH = 'efectivo', 'Efectivo'
        TRANSFER = 'transferencia', 'Transferencia / SPEI'
        OXXO = 'oxxo', 'Depósito OXXO'
        OTHER = 'otro', 'Otro / A definir'

    customer_name = models.CharField('nombre del cliente', max_length=120)
    phone = models.CharField('teléfono / WhatsApp', max_length=20)
    delivery_place = models.CharField('lugar de entrega', max_length=180, blank=True)
    delivery_datetime = models.DateTimeField('fecha/hora deseada', blank=True, null=True)
    payment_method = models.CharField(
        'método de pago',
        max_length=20,
        choices=PaymentMethod.choices,
        blank=True,
    )
    notes = models.TextField('notas adicionales', blank=True)
    status = models.CharField('estado', max_length=20, choices=Status.choices, default=Status.PENDING)
    whatsapp_message = models.TextField('mensaje de WhatsApp generado', blank=True)
    created_at = models.DateTimeField('creado', auto_now_add=True)
    updated_at = models.DateTimeField('actualizado', auto_now=True)

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['-created_at']

    def __str__(self):
        return f'Pedido #{self.pk} — {self.customer_name}'

    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='items', verbose_name='pedido')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items', verbose_name='producto')
    quantity = models.PositiveIntegerField('cantidad', default=1)
    unit_price = models.DecimalField('precio unitario', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'producto del pedido'
        verbose_name_plural = 'productos del pedido'

    def __str__(self):
        return f'{self.product} x{self.quantity}'

    @property
    def subtotal(self):
        return self.quantity * self.unit_price
