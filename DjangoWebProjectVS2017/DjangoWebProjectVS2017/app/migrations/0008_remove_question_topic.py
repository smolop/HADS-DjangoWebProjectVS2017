# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-18 07:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='topic',
        ),
    ]
