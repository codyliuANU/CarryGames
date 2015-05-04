# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0020_auto_20150503_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='result_user1',
            field=models.CharField(null=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='match',
            name='result_user2',
            field=models.CharField(null=True, max_length=10),
        ),
    ]
