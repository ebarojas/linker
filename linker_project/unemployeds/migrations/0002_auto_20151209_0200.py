# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unemployeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unemployed',
            name='location',
            field=models.CharField(default=b'', max_length=80),
        ),
        migrations.AddField(
            model_name='unemployed',
            name='resume',
            field=models.CharField(default='You only live once', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unemployed',
            name='headline',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='unemployed',
            name='location_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='unemployed',
            name='location_lon',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='unemployed',
            name='num_connections',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unemployed',
            name='phone',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='unemployed',
            name='picture_url',
            field=models.CharField(default=b'http://www.komarketingassociates.com/images/2014/08/linkedin-default.png', max_length=320),
        ),
    ]
