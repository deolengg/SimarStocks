# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-07 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraphToDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=42)),
                ('three', models.FloatField()),
                ('twelve', models.FloatField()),
                ('thirtySix', models.FloatField()),
            ],
        ),
    ]
