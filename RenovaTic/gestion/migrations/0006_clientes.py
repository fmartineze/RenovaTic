# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_auto_20161111_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('nombre_cliente', models.CharField(max_length=250, primary_key=True, serialize=False, verbose_name='Razon Social')),
                ('email', models.EmailField(default='user@domain.es', max_length=254, verbose_name='Email')),
                ('web', models.URLField(default='', verbose_name='Sitio web')),
            ],
        ),
    ]