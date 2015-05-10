# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0024_match_current_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='temp_score_user1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='temp_score_user2',
            field=models.IntegerField(default=0),
        ),
    ]
