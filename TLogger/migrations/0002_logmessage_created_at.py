# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TLogger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 10, 10, 50, 52, 694439, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
