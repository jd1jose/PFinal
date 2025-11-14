from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre