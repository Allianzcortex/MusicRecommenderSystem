# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20160309_0931'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='reply',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='agree_count',
            field=models.IntegerField(default=0),
        ),
    ]