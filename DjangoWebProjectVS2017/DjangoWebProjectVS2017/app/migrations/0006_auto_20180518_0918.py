# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-18 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180518_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.CharField(max_length=200),
        ),
    ]
