# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_idea_displayed'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='title',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
