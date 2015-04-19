# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0014_auto_20150410_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='background',
            field=models.ImageField(upload_to='tournaments_background/'),
            preserve_default=True,
        ),
    ]
