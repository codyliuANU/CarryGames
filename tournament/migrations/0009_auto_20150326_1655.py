# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0008_auto_20150326_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='round',
            field=models.ForeignKey(to='tournament.Round', related_name='matches', null=True),
            preserve_default=True,
        ),
    ]
