from rest_framework import serializers
import tournament
from tournament.models import Contestant, Match, Attendant, TournamentData, Conference, Round, Properties


class ContestantSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='account.id')

    class Meta:
        model = Contestant
        fields = ('id', 'score')


class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tournament.models.Meta
        fields = ('matchId', 'UIShiftDown', 'matchType')


class MatchSerializer(serializers.ModelSerializer):
    team1 = ContestantSerializer(source='contestant1')
    team2 = ContestantSerializer(source='contestant2')
    meta = MetaSerializer()

    class Meta:
        model = Match
        fields = ('team1', 'team2', 'meta')


class RoundField(serializers.Field):
    def to_representation(self, obj):
        conference_pk = obj.instance.pk
        rounds = Round.objects.filter(conference=conference_pk)
        return [MatchSerializer(r.matches, many=True).data for r in rounds]

    def to_internal_value(self, data):
        return 1 #TODO: Implement method that convert json to python object


class RoundSerializer(serializers.ModelSerializer):
    matches = MatchSerializer(many=True)

    class Meta:
        model = Round
        fields = ('matches',)


class ConferenceSerializer(serializers.ModelSerializer):
    matches = RoundField(source='rounds')

    class Meta:
        model = Conference
        fields = ('matches',)


class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ('status', 'unbalanced')


class TournamentDataSerializer(serializers.ModelSerializer):
    conferences = ConferenceSerializer(many=True)
    properties = PropertiesSerializer()

    class Meta:
        model = TournamentData
        fields = ('type', 'conferences', 'properties')


class AttendantSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='account.battle_tag')
    id = serializers.ReadOnlyField(source='account.id')
    flag = serializers.ReadOnlyField(source='gameClass')

    class Meta:
        model = Attendant
        fields = ('name', 'id', 'flag')


