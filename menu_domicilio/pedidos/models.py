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
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Se guarda la fecha/hora actual al crear el pedido

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.user.username}"
