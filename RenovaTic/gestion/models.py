from __future__ import unicode_literals

from django.db import models

class Tipo_productos(models.Model):
    nombre_tipo = models.CharField(max_length=100)

    descripcion = models.TextField()
class Proveedores(models.Model):
    nombre_proveedor = models.CharField(max_length=200)
    descripcion = models.TextField()

class Productos(models.Model):
    nombre_producto = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio_comra = models.FloatField()
    precio_venta = models.FloatField()
    proveedor = models.ForeignKey(Proveedores)
    tipo = models.ForeignKey(Tipo_productos)

# Create your models here.
