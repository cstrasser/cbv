# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0012_auto_20170127_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='m8_parent_uuid',
            field=models.CharField(default='', editable=False, max_length=38),
        ),
    ]