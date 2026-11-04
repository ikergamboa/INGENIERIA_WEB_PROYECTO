from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    path('cocina/', views.panel_cocina, name='panel_cocina'),
]