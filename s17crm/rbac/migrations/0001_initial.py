# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('url', models.CharField(max_length=256, verbose_name='正则 url')),
                ('code', models.CharField(max_length=16, verbose_name='权限代号')),
                ('is_menu', models.BooleanField(verbose_name='是否是菜单')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Group', verbose_name='权限分组')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('permissions', models.ManyToManyField(to='rbac.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('roles', models.ManyToManyField(to='rbac.Role')),
            ],
        ),
    ]