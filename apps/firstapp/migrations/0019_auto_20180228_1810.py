# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0018_auto_20180228_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
