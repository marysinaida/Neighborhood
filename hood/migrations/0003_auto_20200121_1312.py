# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-21 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20200120_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='hood',
        ),
        migrations.RemoveField(
            model_name='business',
            name='user',
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
        migrations.RemoveField(
            model_name='neighborhood',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='post',
            name='hood',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='hood',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.DeleteModel(
            name='Neighborhood',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]