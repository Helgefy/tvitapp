# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 12:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gatherer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tweets',
            new_name='Tweet',
        ),
    ]
