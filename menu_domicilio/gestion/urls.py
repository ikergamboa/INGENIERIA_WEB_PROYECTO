from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    path('cocina/', views.panel_cocina, name='panel_cocina'),
    path('registro/', views.registro, name='registro'),
    path('registro/exito/', views.registro_exito, name='registro_exito'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('cocina/crear/', views.crear_plato, name='crear_plato'),
    path('cocina/editar/<int:plato_id>/', views.editar_plato, name='editar_plato'),
    path('cocina/borrar/<int:plato_id>/', views.borrar_plato, name='borrar_plato'),
]