# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20170716_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Skipped'), (2, 'Shared')], default=0, max_length=1),
        ),
    ]
