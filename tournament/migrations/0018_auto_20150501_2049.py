# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0017_auto_20150423_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournamentdata',
            name='tournament',
        ),
        migrations.AddField(
            model_name='tournament',
            name='t_data',
            field=models.OneToOneField(to='tournament.TournamentData', null=True),
        ),
    ]
