from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    path('cocina/', views.panel_cocina, name='panel_cocina'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
]