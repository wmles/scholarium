# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-20 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170220_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholariumprofile',
            name='kaeufe',
            field=models.ManyToManyField(editable=False, through='accounts.Kauf', to='Produkte.Produkt'),
        ),
    ]