# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0022_auto_20150504_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='mode',
            field=models.CharField(default='Bo3', max_length=5),
            preserve_default=False,
        ),
    ]
