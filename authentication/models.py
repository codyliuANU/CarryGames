from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, battle_tag, account_id, password=None, **kwargs):
        if not battle_tag:
            raise ValueError('Пользователь должен иметь корректный BattleTag.')
        if not account_id:
            raise ValueError('Пользователь должен иметь корректный Battle.NET ID.')

        email = self.normalize_email(kwargs.get('email'))
        account = self.model(
            battle_tag=battle_tag,
            account_id=account_id,
            email=email if email is not None else ''
        )
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, battle_tag, account_id, password, **kwargs):
        account = self.create_user(battle_tag, account_id, password, **kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    battle_tag = models.CharField(max_length=15, unique=True)
    account_id = models.BigIntegerField()  # Id from battle.net

    email = models.EmailField(unique=True)

    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Django admin required
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    flag = models.CharField(max_length=20)

    objects = AccountManager()

    USERNAME_FIELD = 'battle_tag'
    REQUIRED_FIELDS = ['account_id']

    def __unicode__(self):
        return self.battle_tag

    def get_full_name(self):
        return ' '.join([self.battle_tag, self.email])

    def get_short_name(self):
        return self.battle_tag

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
