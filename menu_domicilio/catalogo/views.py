#from django.http import HttpResponse
#from django.shortcuts import render
from .models import Plato
from django.views.generic import ListView

# def menus_disponibles(request):
#     # Consultamos todos los platos de la base de datos (QuerySet API)
#     platos = Plato.objects.all()
    
#     # Enviamos los datos a la plantilla HTML
#     return render(request, 'catalogo/menus.html', {'platos': platos})

#SUSITUIR POR LA FUNCION ANTERIOR
class MenusDisponiblesView(ListView):
    # model define sobre qué tabla de la BD se hace la consulta (equivale a Plato.objects.all())
    model = Plato 
    
    # template_name sobrescribe la plantilla por defecto para usar la tuya
    template_name = 'catalogo/menus.html' 
    
    # context_object_name define el nombre de la variable que recibirá el HTML
    context_object_name = 'platos'
