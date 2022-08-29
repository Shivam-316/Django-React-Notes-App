from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class AuthorManager(UserManager):
    pass

class Author(AbstractUser):
    objects = AuthorManager()