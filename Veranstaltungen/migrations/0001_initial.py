# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-25 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtDerVeranstaltung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=30)),
                ('zeit_erstellt', models.DateTimeField(auto_now_add=True)),
                ('preis_praesenz', models.SmallIntegerField()),
                ('preis_livestream', models.SmallIntegerField()),
                ('preis_aufzeichnung', models.SmallIntegerField()),
                ('zeit_beginn', models.TimeField()),
                ('zeit_ende', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Veranstaltung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=30)),
                ('zeit_erstellt', models.DateTimeField(auto_now_add=True)),
                ('beschreibung', models.TextField(max_length=500)),
                ('datum', models.DateField()),
                ('aufzeichnung', models.FileField(blank=True, null=True, upload_to='')),
                ('art_veranstaltung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Veranstaltungen.ArtDerVeranstaltung')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
