# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unemployed',
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
    ]
