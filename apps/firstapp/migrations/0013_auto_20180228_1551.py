# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_auto_20180228_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='ideas_liked', to='firstapp.User'),
        ),
    ]