# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0019_auto_20150501_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='result_user1',
            field=models.CharField(max_length=10, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='result_user2',
            field=models.CharField(max_length=10, default=0),
            preserve_default=False,
        ),
    ]
