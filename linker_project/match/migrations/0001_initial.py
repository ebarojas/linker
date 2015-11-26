# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('headhunter', '0001_initial'),
        ('unemployed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadhunterLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('headhunter', models.ForeignKey(to='headhunter.Headhunter')),
                ('unemployed', models.ForeignKey(to='unemployed.Unemployed')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('headhunter', models.ForeignKey(to='headhunter.Headhunter')),
                ('unemployed', models.ForeignKey(to='unemployed.Unemployed')),
            ],
        ),
        migrations.CreateModel(
            name='UnemployedLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('headhunter', models.ForeignKey(to='headhunter.Headhunter')),
                ('unemployed', models.ForeignKey(to='unemployed.Unemployed')),
            ],
        ),
    ]
