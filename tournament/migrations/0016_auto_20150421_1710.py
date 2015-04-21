# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0015_auto_20150410_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='background',
            field=models.ImageField(null=True, upload_to='tournaments_background/'),
        ),
    ]
