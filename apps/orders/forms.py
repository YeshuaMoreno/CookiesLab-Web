from django import forms
from .models import CustomerOrder


class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ['customer_name', 'phone', 'delivery_place', 'delivery_datetime', 'notes']
        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Tu WhatsApp'}),
            'delivery_place': forms.TextInput(attrs={'placeholder': 'Facultad, punto de entrega o dirección'}),
            'delivery_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Sabores, horario, método de pago o detalles extra'}),
        }
