# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatherer', '0003_auto_20170907_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='html',
            field=models.TextField(default='asdsad'),
            preserve_default=False,
        ),
    ]
