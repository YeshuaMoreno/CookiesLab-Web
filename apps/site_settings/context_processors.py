from .models import BusinessSettings


def business_settings(request):
    return {'business': BusinessSettings.get_solo()}
