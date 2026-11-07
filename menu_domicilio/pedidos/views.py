from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pedido


@login_required
def mis_pedidos(request):
    # Obtenemos el cliente asociado al usuario actual de la sesión
    cliente_actual = request.user.cliente
    
    # Filtramos los pedidos que pertenecen exclusivamente a este cliente
    pedidos = Pedido.objects.filter(cliente=cliente_actual)
    
    return render(request, 'pedidos/mis_pedidos.html', {'pedidos': pedidos})
