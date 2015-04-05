from rest_framework import viewsets
from rest_framework.response import Response
from tournament.models import Match, Attendant, TournamentData
from tournament.serializers import MatchSerializer, AttendantSerializer, TournamentDataSerializer


class MatchViewSet(viewsets.GenericViewSet):

    queryset = Match.objects.all()

    def retrieve(self, request, pk=None):
        queryset = Match.objects.filter(tournament=pk)
        serializer = AttendantSerializer(queryset, many=True)
        return Response(serializer.data)


class AttendantViewSet(viewsets.GenericViewSet):

    queryset = Attendant.objects.all()

    def retrieve(self, request, pk=None):
        queryset = Attendant.objects.filter(tournament=pk)
        serializer = AttendantSerializer(queryset, many=True)
        return Response(serializer.data)


class TournamentDataViewSet(viewsets.GenericViewSet):

    queryset = TournamentData.objects.all()

    def retrieve(self, request, pk=None):
        queryset = TournamentData.objects.get(tournament=pk)
        return Response(TournamentDataSerializer(queryset).data)