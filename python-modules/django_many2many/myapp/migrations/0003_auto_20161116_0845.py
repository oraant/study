# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-16 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_group_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='sex',
            field=models.CharField(default='M', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(default='M', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='sex',
            field=models.CharField(default='M', max_length=50),
            preserve_default=False,
        ),
    ]