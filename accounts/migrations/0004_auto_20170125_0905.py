# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-25 09:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170124_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholariumprofile',
            name='anrede',
            field=models.CharField(choices=[('Herr', 'Herr'), ('Frau', 'Frau')], default='Herr', max_length=4),
        ),
        migrations.AddField(
            model_name='scholariumprofile',
            name='firma',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='scholariumprofile',
            name='land',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='scholariumprofile',
            name='ort',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='scholariumprofile',
            name='plz',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(5)]),
        ),
        migrations.AddField(
            model_name='scholariumprofile',
            name='strasse',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='scholariumprofile',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
