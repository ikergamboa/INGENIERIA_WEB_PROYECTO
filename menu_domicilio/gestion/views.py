from django.http import HttpResponse
from catalogo.models import Plato

def panel_cocina(request):
    # 1. Recuperamos todos los platos de la base de datos
    platos = Plato.objects.all()
    
    # 2. Creamos una variable de texto y le sumamos la información
    texto = "Panel de Cocina - Platos en el sistema:<br><br>"
    
    for plato in platos:
        # Añadimos cada plato al texto con un salto de línea (<br>)
        texto += f"- {plato.nombre} | Categoría: {plato.categoria} | Stock: {plato.num_disponible}<br>"
        
    # 3. Devolvemos el texto final construido al navegador
    return HttpResponse(texto)