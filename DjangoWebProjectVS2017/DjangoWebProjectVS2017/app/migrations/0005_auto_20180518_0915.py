# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-18 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_polltheme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, unique=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='polltheme',
            name='question',
        ),
        migrations.RemoveField(
            model_name='polltheme',
            name='theme',
        ),
        migrations.DeleteModel(
            name='PollTheme',
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(default='Default', on_delete=django.db.models.deletion.CASCADE, to='app.Topic'),
            preserve_default=False,
        ),
    ]