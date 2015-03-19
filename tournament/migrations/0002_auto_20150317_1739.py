# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('conference', models.ForeignKey(to='tournament.Conference')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='match',
            name='conference',
        ),
        migrations.AddField(
            model_name='match',
            name='round',
            field=models.ForeignKey(to='tournament.Round', default=1),
            preserve_default=False,
        ),
    ]
