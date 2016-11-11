# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20161111_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='id',
        ),
        migrations.RemoveField(
            model_name='proveedores',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tipo_productos',
            name='id',
        ),
        migrations.AlterField(
            model_name='productos',
            name='nombre_producto',
            field=models.CharField(max_length=250, primary_key=True, serialize=False, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='nombre_proveedor',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='tipo_productos',
            name='nombre_tipo',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Nombre'),
        ),
    ]