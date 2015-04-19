# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_auto_20150318_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='unbalanced',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
