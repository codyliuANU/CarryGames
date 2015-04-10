# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournament', '0011_auto_20150405_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='account',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='allmatches',
            field=models.CharField(max_length=3, default='Bo3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 4, 9, 17, 26, 57, 491925, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='fare',
            field=models.IntegerField(max_length=4, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='finals',
            field=models.CharField(max_length=3, default='Bo5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='maxplayers',
            field=models.PositiveIntegerField(max_length=3, default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='rules',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='semi',
            field=models.CharField(max_length=3, default='Bo3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 4, 9, 17, 28, 21, 723176, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
