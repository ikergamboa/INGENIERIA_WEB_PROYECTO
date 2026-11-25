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
    
    return render(request, 'Pedidos/mis_pedidos.html', {'pedidos': pedidos})

@login_required
def hacer_pedido(request, plato_id):
    if request.method == 'POST':
        # Comprobar si el usuario actual tiene un perfil de cliente asociado
        if not hasattr(request.user, 'cliente'):
            # Si es un superusuario/admin sin perfil de cliente
            return redirect('catalogo:menus_disponibles')

        plato = get_object_or_404(Plato, pk=plato_id)
        # Validamos la cantidad en el servidor: debe ser un entero mayor o igual que 1
        try:
            cantidad = int(request.POST.get('cantidad', 1))
        except (TypeError, ValueError):
            return redirect('catalogo:menus_disponibles')

        if cantidad < 1:
            return redirect('catalogo:menus_disponibles')

        if plato.num_disponible >= cantidad:
            plato.num_disponible -= cantidad
            plato.save()

            Pedido.objects.create(
                cliente=request.user.cliente,
                plato=plato,
                cantidad=cantidad
            )

            return redirect('pedidos:mis_pedidos')

    return redirect('catalogo:menus_disponibles')
