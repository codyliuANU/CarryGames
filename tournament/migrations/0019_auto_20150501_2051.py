# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0018_auto_20150501_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='t_data',
            field=models.OneToOneField(to='tournament.TournamentData'),
        ),
    ]
