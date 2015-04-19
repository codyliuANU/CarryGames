# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_auto_20150317_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='tournamentData',
        ),
        migrations.AddField(
            model_name='tournamentdata',
            name='properties',
            field=models.OneToOneField(to='tournament.Properties', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conference',
            name='tournamentData',
            field=models.ForeignKey(to='tournament.TournamentData', related_name='conferences'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='round',
            field=models.ForeignKey(to='tournament.Round', related_name='matches'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='round',
            name='conference',
            field=models.ForeignKey(to='tournament.Conference', related_name='rounds'),
            preserve_default=True,
        ),
    ]
