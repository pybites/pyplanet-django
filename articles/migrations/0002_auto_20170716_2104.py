# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='action',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article',
            new_name='title',
        ),
    ]
