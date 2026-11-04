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
    disponible = models.BooleanField(default=True, verbose_name="Disponible")

    def __str__(self):
        return f"{self.nombre}"