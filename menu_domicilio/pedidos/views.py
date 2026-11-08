from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pedido
from catalogo.models import Plato

@login_required
def mis_pedidos(request):
    # Obtenemos el cliente asociado al usuario actual de la sesión
    cliente_actual = request.user.cliente
    
    # Filtramos los pedidos que pertenecen exclusivamente a este cliente
    pedidos = Pedido.objects.filter(cliente=cliente_actual)
    
    return render(request, 'pedidos/mis_pedidos.html', {'pedidos': pedidos})

@login_required
def hacer_pedido(request, plato_id):
    if request.method == 'POST':
        plato = get_object_or_404(Plato, pk=plato_id)
        cantidad = int(request.POST.get('cantidad', 1))

        # Comprobamos que haya stock suficiente
        if plato.num_disponible >= cantidad:
            # 1. Descontamos el stock y guardamos el plato
            plato.num_disponible -= cantidad
            plato.save()

            # 2. Creamos el pedido asignando el plato y la cantidad
            cliente_actual = request.user.cliente
            Pedido.objects.create(
                cliente=cliente_actual,
                plato=plato,           # <-- AQUÍ: pasamos la instancia del plato
                cantidad=cantidad       # <-- y la cantidad pedida
            )

            return redirect('pedidos:mis_pedidos')

    return redirect('catalogo:menus_disponibles')
