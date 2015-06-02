from rest_framework import viewsets, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import Account
from authentication.serializers import AccountSerializer
from battlenet.oauth2 import BattleNetOAuth2
from djoser.serializers import TokenSerializer


class AccountViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    #permission_classes = [permissions]


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = (permissions.AllowAny,)
    serializer_class = AuthTokenSerializer
    model = Token

    def post(self, request):
        try:
            bnet = BattleNetOAuth2(redirect_uri="https://127.0.0.1:8000/authcode/", scope='')
            bnet_token = bnet.retrieve_access_token(request.DATA['auth_code'])
            if bnet_token is not None:
                accountId = bnet_token['accountId']
                battle_tag = bnet.get_battletag()[1]['battletag']
                user = get_account_by_bnet_id(account_id=accountId, battle_tag=battle_tag)

        except ValueError as e:
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                data=TokenSerializer(token).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response("User was not found.", status=status.HTTP_400_BAD_REQUEST)


def get_account_by_bnet_id(account_id, battle_tag):
    if account_id is None or battle_tag is None:
        raise ValueError("AccountId or BattleTag is not define.")
    acc = None
    try:
        acc = Account.objects.get(account_id=account_id)
        if acc.battle_tag != battle_tag:
            acc.battle_tag = battle_tag
            acc.save()
        return acc
    except Account.DoesNotExist:
        pass

    if acc is None:
        new_account = Account.objects.create_user(battle_tag=battle_tag, account_id=account_id)
        new_account.save()
        return new_account
