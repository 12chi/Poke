# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-31 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0005_poke_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tot_count',
            field=models.IntegerField(default=0),
        ),
    ]
