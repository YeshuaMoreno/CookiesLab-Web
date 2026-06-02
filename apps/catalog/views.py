from django.shortcuts import render
from .models import Category, Product


def menu(request):
    categories = Category.objects.filter(is_active=True).prefetch_related('products')
    products = Product.objects.exclude(status=Product.Status.HIDDEN).select_related('category')
    return render(request, 'catalog/menu.html', {
        'categories': categories,
        'products': products,
    })
