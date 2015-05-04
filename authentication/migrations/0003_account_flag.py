# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20150421_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='flag',
            field=models.CharField(default='rus.png', max_length=20),
            preserve_default=False,
        ),
    ]
