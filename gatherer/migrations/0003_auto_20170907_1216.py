# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gatherer', '0002_auto_20170907_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='publishdate',
            new_name='publish_date',
        ),
    ]
