# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0007_auto_20150325_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='reporter',
            field=models.ForeignKey(to='tournament.Reporter', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='round',
            name='conference',
            field=models.ForeignKey(to='tournament.Conference', null=True, related_name='rounds'),
            preserve_default=True,
        ),
    ]
