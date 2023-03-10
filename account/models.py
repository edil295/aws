from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
