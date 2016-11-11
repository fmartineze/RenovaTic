from __future__ import unicode_literals

from django.db import models

class Tipo_productos(models.Model):
    nombre_tipo = models.CharField('Nombre', max_length=100, primary_key=True)
    descripcion = models.TextField('Descripcion')
    def __unicode__(self):
        return self.pk

class Proveedores(models.Model):
    nombre_proveedor = models.CharField('Nombre', max_length=200, primary_key=True)
    email = models.EmailField('Email', default='user@domain.es')
    web = models.URLField('Sitio web', default='')
    descripcion = models.TextField('Descripcion')
    def __unicode__(self):
        return self.pk

class Productos(models.Model):
    nombre_producto = models.CharField('Nombre', max_length=250, primary_key=True)
    descripcion = models.TextField('Descripcion')
    precio_compra = models.FloatField('precio compra')
    precio_venta = models.FloatField('precio venta')
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_productos, on_delete=models.CASCADE)

    def _magen(self):
        return self.precio_venta - self.precio_compra

    magen = property(_magen)

    def __unicode__(self):
        return self.pk

class Clientes(models.Model):
    nombre_cliente = models.CharField('Razon Social', max_length=250, primary_key=True)
    email = models.EmailField('Email', default='user@domain.es')
    web = models.URLField('Sitio web', default='')
    
    def __unicode__(self):
        return self.pk

# Create your models here.
