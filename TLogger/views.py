from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from TLogger.models import LogManager
from TLogger.serializers import LogManagerSerializer


class LogManagerViewSet(viewsets.ModelViewSet):
    serializer_class = LogManagerSerializer
    queryset = LogManager.objects.all()

    # def list(self, request):
    #     queryset = LogManager.objects.all()
    #     serializer = LogManagerSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = LogManager.objects.all()
    #     log_manager = get_object_or_404(queryset, pk=pk)
    #     serializer = LogManagerSerializer(log_manager)
    #     return Response(serializer.data)


