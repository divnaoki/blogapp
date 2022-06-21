from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Accounts(AbstractBaseUser):
  username = models.CharField(
    max_length=20,
    null=False
  )
  email = models.EmailField(
    max_length=255,
    null=False,
    unique=True
  )
  birthday = models.DateField()
  is_active = models.BooleanField(
    default=True
  )
  profile = models.CharField(
    max_length=300,
    default="comming soon"
  )