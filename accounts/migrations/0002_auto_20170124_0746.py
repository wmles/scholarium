# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-24 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyProfile',
            new_name='ScholariumProfile',
        ),
    ]
