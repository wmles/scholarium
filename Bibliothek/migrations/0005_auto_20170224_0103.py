# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-24 01:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bibliothek', '0004_buch_exlibris'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buch',
            options={'verbose_name_plural': 'Bücher'},
        ),
    ]