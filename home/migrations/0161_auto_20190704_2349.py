# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-04 23:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0160_copy_apps_contributions_dates'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participation',
            options={'ordering': ('community__name',)},
        ),
    ]