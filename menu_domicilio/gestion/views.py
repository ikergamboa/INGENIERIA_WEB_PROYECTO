from django.http import HttpResponse
from catalogo.models import Plato

def panel_cocina(request):
    platos = Plato.objects.all()
    
    texto = "Panel de Cocina - Platos en el sistema:<br><br>"
    
    for plato in platos:
        texto += f"- {plato.nombre} | Categoría: {plato.categoria} | Stock: {plato.num_disponible}<br>"
        
    return HttpResponse(texto)