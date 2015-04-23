# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0016_auto_20150421_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 17, 15, 14, 936861, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='region',
            field=models.CharField(default='Europe', max_length=30),
            preserve_default=False,
        ),
    ]
