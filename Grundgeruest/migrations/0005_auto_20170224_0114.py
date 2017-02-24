# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-24 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grundgeruest', '0004_ganzesmenue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ganzesmenue',
            name='gehoert_zu',
        ),
        migrations.AddField(
            model_name='hauptpunkt',
            name='gehoert_zu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Grundgeruest.GanzesMenue'),
            preserve_default=False,
        ),
    ]
