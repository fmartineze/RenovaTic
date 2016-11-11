from __future__ import unicode_literals

from django.db import models

class Tipo_productos(models.Model):
    nombre_tipo = models.CharField('Nombre', max_length=100, primary_key=True)
    descripcion = models.TextField('Descripcion')
    def __unicode__(self):
        return self.pk
    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"

class Proveedores(models.Model):
    nombre_proveedor = models.CharField('Nombre', max_length=200, primary_key=True)
    email = models.EmailField('Email', default='user@domain.es')
    web = models.URLField('Sitio web', default='')
    descripcion = models.TextField('Descripcion')
    def __unicode__(self):
        return self.pk
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Productos(models.Model):
    nombre_producto = models.CharField('Nombre', max_length=250, primary_key=True)
    descripcion = models.TextField('Descripcion')
    precio_compra = models.FloatField('precio compra')
    precio_venta = models.FloatField('precio venta')
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name="Proveedor")
    tipo = models.ForeignKey(Tipo_productos, on_delete=models.CASCADE, verbose_name="Tipo de Producto")
    def __unicode__(self):
        return self.pk
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Clientes(models.Model):
    nombre_cliente = models.CharField('Razon Social', max_length=250, primary_key=True)
    email = models.EmailField('Email', default='user@domain.es')
    web = models.URLField('Sitio web', default='')

    def __unicode__(self):
        return self.pk
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Renovaciones(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name="Cliente")
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, verbose_name="Producto")
    fecha_inicio = models.DateField('Fecha de Inicio')
    fecha_renovacion = models.DateField('Proxima renovacion')
    descripcion = models.TextField('Descripcion')

    class Meta:
        verbose_name = "Renovacion"
        verbose_name_plural = "Renovaciones"
