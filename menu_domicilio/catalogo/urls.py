from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
 path('menus/', views.menus_disponibles, name='menus_disponibles'),
]