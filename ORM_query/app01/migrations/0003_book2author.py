# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20170914_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book2Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Book')),
            ],
        ),
    ]
