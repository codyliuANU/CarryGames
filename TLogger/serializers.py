from rest_framework import serializers
from TLogger.models import LogMessage, LogManager
from authentication.serializers import AccountSerializer


class LogMessageSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=25, source='author.battle_tag')

    class Meta:
        model = LogMessage
        fields = ('message', 'author', 'created_at',)


class LogManagerSerializer(serializers.ModelSerializer):
    log_messages = LogMessageSerializer(many=True, source='logmessage_set')

    class Meta:
        model = LogManager
        fields = ('log_messages',)

