# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0010_auto_20161111_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renovaciones',
            name='id',
        ),
        migrations.AlterField(
            model_name='renovaciones',
            name='nombre_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gestion.Clientes', verbose_name='Nombre de Cliente'),
        ),
    ]
