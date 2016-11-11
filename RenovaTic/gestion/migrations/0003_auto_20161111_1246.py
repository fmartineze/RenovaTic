# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20161111_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='nombre_producto',
            field=models.CharField(max_length=250, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio_comra',
            field=models.FloatField(verbose_name='precio compra'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio_venta',
            field=models.FloatField(verbose_name='precio venta'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='email',
            field=models.EmailField(default='user@domain.es', max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='nombre_proveedor',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='web',
            field=models.URLField(default='', verbose_name='Sitio web'),
        ),
        migrations.AlterField(
            model_name='tipo_productos',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='tipo_productos',
            name='nombre_tipo',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]