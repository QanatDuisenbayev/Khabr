# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-03-27 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import habr.models


class Migration(migrations.Migration):

    dependencies = [
        ('habr', '0003_auto_20190326_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=habr.models.generic_filename),
        ),
    ]
