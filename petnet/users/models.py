from django.contrib.auth.models import User
from django.db import models


class User(User):
    avatar = models.ImageField(null=True, blank=True)


