# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0021_auto_20150503_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='reporter',
        ),
        migrations.AddField(
            model_name='match',
            name='status',
            field=models.CharField(default='Created', max_length=15),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
