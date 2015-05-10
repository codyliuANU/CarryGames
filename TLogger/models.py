from django.db import models
from authentication.models import Account


class LogManager(models.Model):
    pass


class LogMessage(models.Model):
    manager = models.ForeignKey(LogManager)
    author = models.OneToOneField(Account)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
