# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TLogger', '0001_initial'),
        ('tournament', '0025_auto_20150504_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='log_manager',
            field=models.OneToOneField(to='TLogger.LogManager', null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='log_manager',
            field=models.OneToOneField(to='TLogger.LogManager', null=True),
        ),
    ]
