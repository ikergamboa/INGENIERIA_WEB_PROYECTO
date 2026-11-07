from django.urls import path
from . import views


app_name = 'pedidos'

urlpatterns = [
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
]
