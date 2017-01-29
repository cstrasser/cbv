# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-25 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0006_company_isvendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_contact',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quote.Company'),
        ),
        migrations.AlterField(
            model_name='company_contact',
            name='company_uuid',
            field=models.CharField(blank=True, max_length=36),
        ),
    ]
