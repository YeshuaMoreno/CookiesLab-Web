from django.urls import path
from . import views

app_name = 'promos'

urlpatterns = [
    path('', views.promos_list, name='list'),
]
