from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.create_order, name='create'),
    path('gracias/', views.order_success, name='success'),
]
