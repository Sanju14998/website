# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-31 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20171231_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='list_project',
            field=models.NullBooleanField(default=None, verbose_name='Coordinators: Check this box once you have reviewed the project information'),
        ),
    ]
