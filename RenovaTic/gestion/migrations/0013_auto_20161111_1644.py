# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0012_auto_20161111_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Renovations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha Inicio')),
                ('nombre_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Clientes', verbose_name='Nombre de Cliente')),
            ],
            options={
                'ordering': ('fecha_inicio',),
                'verbose_name': 'Renovacion',
                'verbose_name_plural': 'Renovaciones',
            },
        ),
        migrations.RemoveField(
            model_name='renovaciones',
            name='nombre_cliente',
        ),
        migrations.DeleteModel(
            name='Renovaciones',
        ),
    ]
