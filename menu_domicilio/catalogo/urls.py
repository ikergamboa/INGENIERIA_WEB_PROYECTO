from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('menus/', views.menus_disponibles, name='menus_disponibles'),
]