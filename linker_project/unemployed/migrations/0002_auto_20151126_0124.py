# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('unemployed', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unemployed',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='unemployed',
            name='headline',
            field=models.CharField(default=datetime.datetime(2015, 11, 26, 1, 24, 42, 759084, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unemployed',
            name='linkedin_id',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unemployed',
            name='num_connections',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unemployed',
            name='picture_url',
            field=models.CharField(default='', max_length=320),
            preserve_default=False,
        ),
    ]
