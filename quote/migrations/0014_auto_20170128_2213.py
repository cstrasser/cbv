# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0013_auto_20170127_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='parent_company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quote.Company'),
        ),
    ]
