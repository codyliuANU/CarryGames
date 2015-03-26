# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0005_auto_20150319_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='account',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='contestant1',
            field=models.OneToOneField(to='tournament.Contestant', related_name='contestant1', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='contestant2',
            field=models.OneToOneField(to='tournament.Contestant', related_name='contestant2', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meta',
            name='matchType',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
