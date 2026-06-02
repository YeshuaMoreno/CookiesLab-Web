from django.shortcuts import render
from .models import Category, Product


def menu(request):
    categories = Category.objects.filter(is_active=True)
    products = (
        Product.objects
        .exclude(status=Product.Status.HIDDEN)
        .select_related('category')
        .order_by('category__order', 'name')
    )
    return render(request, 'catalog/menu.html', {
        'categories': categories,
        'products': products,
    })
