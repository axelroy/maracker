# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marackerapi', '0007_auto_20170605_1722'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mipapplication',
            unique_together=set([('docker_namespace', 'docker_image')]),
        ),
    ]