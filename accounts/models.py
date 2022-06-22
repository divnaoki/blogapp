from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class Accounts(AbstractBaseUser):
  username = models.CharField(
    max_length=20,
    null=False,
    unique=True
  )
  email = models.EmailField(
    max_length=255,
    null=True,
    unique=True
  )
  birthday = models.DateField(
    null=True
  )
  is_active = models.BooleanField(
    default=True
  )
  profile = models.CharField(
    max_length=300,
    default="comming soon"
  )
  is_staff = models.BooleanField(
    help_text="ユーザーがこの管理サイトにログインできるかどうかを指定します。",
    default=False,
  )
  is_superuser = models.BooleanField(
    default=False
  )
  objects = UserManager()
  USERNAME_FIELD = 'username'
  EMAIL_FIELD = 'email'