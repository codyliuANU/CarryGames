from rest_framework import viewsets, permissions
from rest_framework.response import Response
from tournament.models import Match, Attendant, TournamentData, Tournament
from tournament.serializers import MatchSerializer, AttendantSerializer, TournamentDataSerializer, TournamentSerializer


class MatchViewSet(viewsets.GenericViewSet):

    queryset = Match.objects.all()

    def retrieve(self, request, pk=None):
        queryset = Match.objects.get(id=pk)
        serializer = MatchSerializer(queryset)
        return Response(serializer.data)


class AttendantViewSet(viewsets.ModelViewSet):

    queryset = Attendant.objects.all()
    serializer_class = AttendantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def retrieve(self, request, pk=None):
        queryset = Attendant.objects.filter(tournament=pk)
        serializer = AttendantSerializer(queryset, many=True)
        return Response(serializer.data)


class TournamentDataViewSet(viewsets.GenericViewSet):

    queryset = TournamentData.objects.all()

    def retrieve(self, request, pk=None):
        queryset = TournamentData.objects.get(tournament=pk)
        return Response(TournamentDataSerializer(queryset).data)


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def list(self, request):
    #     qs = self.get_queryset()
    #     return Response(TournamentSerializer(qs, many=True).data)