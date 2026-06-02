from django import forms
from .models import CustomerOrder

_INPUT = 'w-full rounded-2xl border border-gray-200 bg-gray-50 px-4 py-3 text-[#070707] outline-none transition-colors focus:border-[#E50914] focus:ring-2 focus:ring-[#E50914]/10'
_SELECT = _INPUT + ' cursor-pointer'
_TEXTAREA = _INPUT


class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ['customer_name', 'phone', 'delivery_place', 'delivery_datetime', 'payment_method', 'notes']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'placeholder': 'Tu nombre completo',
                'class': _INPUT,
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Tu número de WhatsApp (10 dígitos)',
                'class': _INPUT,
            }),
            'delivery_place': forms.TextInput(attrs={
                'placeholder': 'Facultad, punto de entrega o dirección',
                'class': _INPUT,
            }),
            'delivery_datetime': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': _INPUT,
            }),
            'payment_method': forms.Select(attrs={
                'class': _SELECT,
            }),
            'notes': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Sabores especiales, alergias, horario o cualquier detalle extra…',
                'class': _TEXTAREA,
            }),
        }
        labels = {
            'customer_name': 'Nombre',
            'phone': 'WhatsApp',
            'delivery_place': 'Lugar de entrega',
            'delivery_datetime': 'Fecha y hora (opcional)',
            'payment_method': 'Método de pago',
            'notes': 'Notas adicionales',
        }
