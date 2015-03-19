# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('gameClass', models.CharField(max_length=30)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('score', models.IntegerField(default=0)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('conference', models.ForeignKey(to='tournament.Conference')),
                ('contestant1', models.OneToOneField(related_name='contestant1', to='tournament.Contestant')),
                ('contestant2', models.OneToOneField(related_name='contestant2', to='tournament.Contestant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('matchId', models.CharField(max_length=15)),
                ('UIShiftDown', models.PositiveIntegerField()),
                ('matchType', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('status', models.CharField(max_length=20)),
                ('unbalanced', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TournamentData',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(max_length=10)),
                ('tournament', models.ForeignKey(to='tournament.Tournament')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='properties',
            name='tournamentData',
            field=models.ForeignKey(to='tournament.TournamentData'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='meta',
            field=models.OneToOneField(related_name='meta', to='tournament.Meta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conference',
            name='tournamentData',
            field=models.ForeignKey(to='tournament.TournamentData'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendant',
            name='tournament',
            field=models.ForeignKey(to='tournament.Tournament'),
            preserve_default=True,
        ),
    ]
