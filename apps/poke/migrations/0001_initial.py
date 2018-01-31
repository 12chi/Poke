# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-31 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('pwd', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='poke',
            name='poke_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokes', to='poke.User'),
        ),
        migrations.AddField(
            model_name='poke',
            name='poke_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked', to='poke.User'),
        ),
    ]
