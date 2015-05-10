# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0023_match_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='current_state',
            field=models.IntegerField(default=1),
        ),
    ]
