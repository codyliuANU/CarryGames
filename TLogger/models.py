from django.db import models
from authentication.models import Account


class LogManager(models.Model):
    def log_by_admin(self, message):
        LogMessage(author=Account.objects.get(id=37), manager=self, message=message).save()

    def log(self, user, message):
        LogMessage(author=user, manager=self, message=message).save()


class LogMessage(models.Model):
    manager = models.ForeignKey(LogManager)
    author = models.ForeignKey(Account)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
