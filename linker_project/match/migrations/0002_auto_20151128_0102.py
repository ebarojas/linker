# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('headhunter', '0001_initial'),
        ('unemployed', '0001_initial'),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacantLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('unemployed', models.ForeignKey(to='unemployed.Unemployed')),
                ('vacant', models.ForeignKey(to='headhunter.Vacant')),
            ],
        ),
        migrations.RemoveField(
            model_name='headhunterlike',
            name='headhunter',
        ),
        migrations.RemoveField(
            model_name='headhunterlike',
            name='unemployed',
        ),
        migrations.RemoveField(
            model_name='match',
            name='headhunter',
        ),
        migrations.AddField(
            model_name='match',
            name='vacant',
            field=models.ForeignKey(default=1, to='headhunter.Vacant'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='HeadhunterLike',
        ),
    ]
