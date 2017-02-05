# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-25 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170125_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholariumprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='my_profile', to=settings.AUTH_USER_MODEL, verbose_name='Benutzer'),
        ),
    ]