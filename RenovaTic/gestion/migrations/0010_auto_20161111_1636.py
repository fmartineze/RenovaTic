# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_auto_20161111_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipo_productos',
            options={'verbose_name': 'Familia', 'verbose_name_plural': 'Familias'},
        ),
    ]
