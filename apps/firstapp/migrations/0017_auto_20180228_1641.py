# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0016_auto_20180228_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
    ]
