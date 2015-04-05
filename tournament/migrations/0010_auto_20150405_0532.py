# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0009_auto_20150326_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='score',
            field=models.CharField(max_length=2, default='0'),
            preserve_default=True,
        ),
    ]
