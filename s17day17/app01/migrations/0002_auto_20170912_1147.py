# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 03:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_data',
            new_name='publication_date',
        ),
    ]
