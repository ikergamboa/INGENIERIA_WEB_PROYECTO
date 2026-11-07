from django.http import HttpResponse
from .models import Plato
from django.shortcuts import render

def index(request):
    return HttpResponse("¡Bienvenido a Menu a domicilio!")

def menus_disponibles(request):
    # Consultamos todos los platos de la base de datos (QuerySet API)
    platos = Plato.objects.all()
    
    # Enviamos los datos a la plantilla HTML
    return render(request, 'catalogo/menus.html', {'platos': platos})