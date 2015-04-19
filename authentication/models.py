from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, battle_tag, password=None, **kwargs):
        if not battle_tag:
            raise ValueError('Пользователь должен иметь корректный BattleTag.')

        if not kwargs.get('email'):
            raise ValueError('Пользователь должен иметь корректный email.')

        account = self.model(
            battle_tag=battle_tag,
            email=self.normalize_email(kwargs.get('email'))
        )
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, battle_tag, password, **kwargs):
        account = self.create_user(battle_tag, password, **kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    battle_tag = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Django admin required
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'battle_tag'
    REQUIRED_FIELDS = ['email']

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
