from django.conf.urls import patterns, url, include
from rest_framework import routers
from tournament import views
from tournament.views import MatchViewSet, AttendantViewSet, TournamentDataViewSet, TournamentViewSet


router = routers.SimpleRouter()
router.register(r'matches', MatchViewSet)
router.register(r'attendants', AttendantViewSet)
router.register(r'data', TournamentDataViewSet)
router.register(r'tournaments', TournamentViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)