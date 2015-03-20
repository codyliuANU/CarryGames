from django.db import models
from authentication.models import Account


# Base tournament description
class Tournament(models.Model):
    name = models.CharField(max_length=80)
    # teams: [] (Attendant)
    # tournament: { type: "SE", matches: [] } (TournamentData)


class Properties(models.Model):
    status = models.CharField(max_length=20)
    unbalanced = models.CharField(max_length=10, null=True)


class TournamentData(models.Model):
    type = models.CharField(max_length=10)
    properties = models.OneToOneField(Properties)
    tournament = models.ForeignKey(Tournament)
    # matches: [] (Match)


class Conference(models.Model):
    tournamentData = models.ForeignKey(TournamentData, related_name='conferences')


class Attendant(models.Model):
    account = models.ForeignKey(Account)
    gameClass = models.CharField(max_length=30)
    tournament = models.ForeignKey(Tournament)
############################################


class Contestant(models.Model):
    account = models.ForeignKey(Account)
    score = models.IntegerField(default=0)


class Meta(models.Model):
    matchId = models.CharField(max_length=15)
    UIShiftDown = models.PositiveIntegerField(null=True)
    matchType = models.CharField(max_length=20, null=True)


class Round(models.Model):
    conference = models.ForeignKey(Conference, related_name='rounds')


class Match(models.Model):
    round = models.ForeignKey(Round, related_name='matches')
    contestant1 = models.OneToOneField(Contestant, related_name='contestant1')
    contestant2 = models.OneToOneField(Contestant, related_name='contestant2')
    meta = models.OneToOneField(Meta, related_name='meta')


