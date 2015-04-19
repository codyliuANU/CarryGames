from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from authentication.models import Account
from authentication.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    #permission_classes = [permissions]
