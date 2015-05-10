from django.conf.urls import patterns, url, include
from rest_framework import routers
from TLogger.views import LogManagerViewSet

router = routers.SimpleRouter()
router.register(r'managers', LogManagerViewSet)

urlpatterns = router.urls