# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0020_auto_20161111_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renovaciones',
            name='nombre_cliente',
        ),
        migrations.DeleteModel(
            name='Renovaciones',
        ),
    ]
