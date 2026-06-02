from django.shortcuts import render
from apps.catalog.models import Product
from apps.promos.models import Promotion


def home(request):
    featured_products = Product.objects.filter(is_featured=True).exclude(status=Product.Status.HIDDEN)[:6]
    promotions = [promo for promo in Promotion.objects.all()[:6] if promo.is_current]
    return render(request, 'core/home.html', {
        'featured_products': featured_products,
        'promotions': promotions,
    })
