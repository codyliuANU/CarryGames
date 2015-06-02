# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_account_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
