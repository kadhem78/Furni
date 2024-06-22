from django.db import models
from django.contrib.auth.models import AbstractUser , PermissionsMixin



class CustomUser(AbstractUser , PermissionsMixin) : 
    pass
# Create your models here.
