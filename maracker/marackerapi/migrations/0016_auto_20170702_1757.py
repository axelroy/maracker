# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marackerapi', '0015_auto_20170702_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marackerapplication',
            name='slug',
            field=models.SlugField(max_length=62, unique=True),
        ),
    ]
