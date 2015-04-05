# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0010_auto_20150405_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='score',
            field=models.CharField(default='', max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='contestant1',
            field=models.OneToOneField(related_name='contestant1', default='', to='tournament.Contestant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='contestant2',
            field=models.OneToOneField(related_name='contestant2', default=1, to='tournament.Contestant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meta',
            name='matchType',
            field=models.CharField(null=True, max_length=10),
            preserve_default=True,
        ),
    ]
