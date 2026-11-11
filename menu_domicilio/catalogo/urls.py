from django.urls import path
#from . import views
from .views import MenusDisponiblesView

app_name = 'catalogo'

urlpatterns = [
 #path('menus/', views.menus_disponibles, name='menus_disponibles'),
 #SUSITUIR POR LA LINEA ANTERIOR
 path('menus/', MenusDisponiblesView.as_view(), name='menus_disponibles'),
]