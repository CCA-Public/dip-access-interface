# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 20:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dips', '0007_auto_20171122_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dip',
            name='metsfile',
        ),
    ]
