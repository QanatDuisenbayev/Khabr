# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-03-26 14:17
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habr', '0002_article_comments_useraccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
