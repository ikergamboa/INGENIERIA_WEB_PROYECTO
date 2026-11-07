from django.conf import settings
from django.db import models
from catalogo.models import Plato

# Create your models here.
class Cliente(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cliente')
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Cliente: {self.usuario.get_username()}"

class Pedido(models.Model):
    # ForeignKey define la relación con otro modelo de la base de datos
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now_add=True)
    
    # Es posible indicar un valor por defecto mediante 'default'
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cliente} - {self.plato.nombre}"
