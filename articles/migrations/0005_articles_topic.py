# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_articles_imgpath'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='topic',
            field=models.CharField(default='Transformer', max_length=120),
        ),
    ]
