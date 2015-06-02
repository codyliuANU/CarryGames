from battlenet.oauth2 import BattleNetOAuth2
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tournament.models import Match, Attendant, TournamentData, Tournament, NotAllowedForTheUser
from tournament.serializers import MatchSerializer, AttendantSerializer, TournamentDataSerializer, TournamentSerializer, \
    MatchListSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchListSerializer

    def perform_create(self, serializer):
        pass

    def update(self, request, pk=None):
        try:
            match = Match.objects.get(id=pk)
            match.set_value(request.user, request.data['value_to_setup'])
        except NotAllowedForTheUser as e:
            return Response(str(e), status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = MatchListSerializer(match)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, *args, **kwargs):
        pass


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
        t_data = Tournament.objects.get(id=pk).t_data
        return Response(TournamentDataSerializer(t_data).data)


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def list(self, request):
    #     qs = self.get_queryset()
    #     return Response(TournamentSerializer(qs, many=True).data)
