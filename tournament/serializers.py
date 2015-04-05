from collections import OrderedDict
from rest_framework import serializers
from rest_framework.fields import SkipField
import tournament
from tournament.models import Contestant, Match, Attendant, TournamentData, Conference, Round, Properties


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


class ToTextField(serializers.Field):
    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        return str(value)


class NonNullSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                ret[field.field_name] = field.to_representation(attribute)
            elif field.field_name == "id":
                ret[field.field_name] = ""

        return ret


class ContestantSerializer(NonNullSerializer):
    id = ToTextField(source='account.id')

    class Meta:
        model = Contestant
        fields = ('id', 'score')


class MatchTypeField(serializers.Field):
    def to_representation(self, value):
        try:
            if value.isdigit():
                return num(value)
            else:
                return value
        except AttributeError:
            return value

    def to_internal_value(self, data):
        pass


class MetaSerializer(NonNullSerializer):
    matchType = MatchTypeField()

    class Meta:
        model = tournament.models.Meta
        fields = ('matchId', 'UIShiftDown', 'matchType')


class MatchSerializer(NonNullSerializer):
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


class PropertiesSerializer(NonNullSerializer):
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
    id = ToTextField(source='account.id')
    flag = serializers.ReadOnlyField(source='gameClass')

    class Meta:
        model = Attendant
        fields = ('name', 'id', 'flag')


