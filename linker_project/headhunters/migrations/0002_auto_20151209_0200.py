# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('headhunters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headhunter',
            name='location',
            field=models.CharField(default=b'', max_length=80),
        ),
        migrations.AddField(
            model_name='vacant',
            name='headline',
            field=models.CharField(default='grgr', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacant',
            name='location',
            field=models.CharField(default='Mexico', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='headhunter',
            name='headline',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='headhunter',
            name='location_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='headhunter',
            name='location_lon',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='headhunter',
            name='num_connections',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='headhunter',
            name='phone',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='headhunter',
            name='picture_url',
            field=models.CharField(default=b'http://www.komarketingassociates.com/images/2014/08/linkedin-default.png', max_length=320),
        ),
    ]
