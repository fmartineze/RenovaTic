# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0011_auto_20161111_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renovaciones',
            name='fecha_inicio',
            field=models.DateField(primary_key=True, serialize=False, verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='renovaciones',
            name='nombre_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Clientes', verbose_name='Nombre de Cliente'),
        ),
    ]
