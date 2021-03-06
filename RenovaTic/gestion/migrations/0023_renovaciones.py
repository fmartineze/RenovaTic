# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0022_auto_20161111_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Renovaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de Inicio')),
                ('fecha_renovacion', models.DateField(verbose_name='Proxima renovacion')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Clientes', verbose_name='Cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Productos', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Renovacion',
                'verbose_name_plural': 'Renovaciones',
            },
        ),
    ]
