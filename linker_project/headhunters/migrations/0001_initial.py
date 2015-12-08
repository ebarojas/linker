# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headhunter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=320)),
                ('phone', models.CharField(max_length=10)),
                ('location_lat', models.FloatField()),
                ('location_lon', models.FloatField()),
                ('linkedin_id', models.CharField(max_length=255)),
                ('headline', models.CharField(max_length=255)),
                ('num_connections', models.IntegerField()),
                ('picture_url', models.CharField(max_length=320)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vacant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posted_date', models.DateTimeField(default=datetime.datetime.now)),
                ('location_lat', models.FloatField()),
                ('location_lon', models.FloatField()),
                ('name', models.CharField(max_length=320)),
                ('salary', models.FloatField()),
                ('details', models.CharField(max_length=500)),
                ('picture', models.ImageField(upload_to=b'')),
                ('headhunter', models.ForeignKey(to='headhunters.Headhunter')),
            ],
        ),
    ]
