# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
