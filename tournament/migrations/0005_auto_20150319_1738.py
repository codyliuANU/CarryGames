# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_auto_20150319_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta',
            name='UIShiftDown',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meta',
            name='matchType',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
