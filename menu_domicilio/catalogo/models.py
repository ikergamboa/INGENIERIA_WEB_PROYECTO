from django.db import models

# Create your models here.

class Plato(models.Model):

    CATEGORIAS = [
    ('PRIMERO', 'Primer plato'),
    ('SEGUNDO', 'Segundo plato'),
    ('POSTRE', 'Postre'),
    ('BEBIDA', 'Bebida'),]

    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, verbose_name="Categoría")
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio (€)")
    calorias = models.PositiveIntegerField(verbose_name="Calorías (kcal)")
    num_disponible = models.PositiveIntegerField(default=0, verbose_name="Número disponible")

    # para saber si un plato está disponible 
    @property
    def disponible(self):
        return self.num_disponible > 0

    def __str__(self):
        return f"{self.nombre}"