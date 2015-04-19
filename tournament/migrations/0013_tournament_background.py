# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0012_auto_20150409_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='background',
            field=models.ImageField(default=1, upload_to='tournaments_background'),
            preserve_default=False,
        ),
    ]
