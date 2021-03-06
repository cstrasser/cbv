# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0016_auto_20170130_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='item',
            name='sells_for',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='multiplier',
            field=models.DecimalField(decimal_places=2, default=1.522, max_digits=6),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='poline',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='quote',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
