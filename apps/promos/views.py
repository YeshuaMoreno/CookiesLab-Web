from django.shortcuts import render
from .models import Promotion


def promos_list(request):
    active = [p for p in Promotion.objects.filter(is_active=True).order_by('-created_at') if p.is_current]
    upcoming = Promotion.objects.filter(is_active=True).exclude(
        pk__in=[p.pk for p in active]
    ).order_by('starts_at')
    return render(request, 'promos/list.html', {
        'active_promos': active,
        'upcoming_promos': upcoming,
    })
