# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-19 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesapp', '0002_auto_20180610_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='lat_field',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='long_field',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
    ]
