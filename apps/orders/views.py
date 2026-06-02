from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CustomerOrderForm


def create_order(request):
    if request.method == 'POST':
        form = CustomerOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(request, 'Tu pedido quedó registrado. Te contactaremos por WhatsApp para confirmarlo.')
            return redirect('orders:success')
    else:
        form = CustomerOrderForm()
    return render(request, 'orders/create.html', {'form': form})


def order_success(request):
    return render(request, 'orders/success.html')
