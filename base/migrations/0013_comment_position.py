# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20160426_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
