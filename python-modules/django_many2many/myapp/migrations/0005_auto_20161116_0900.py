# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-16 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20161116_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Group'),
        ),
    ]
