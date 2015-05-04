from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from authentication.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_admin = serializers.CharField(read_only=True)
    is_manager = serializers.CharField(read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'battle_tag', 'email', 'created_at', 'updated_at', 'password', 'is_admin', 'is_manager', 'flag')
        read_only_fields = ('created_at', 'updated_at',)

