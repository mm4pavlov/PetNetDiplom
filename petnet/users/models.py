from django.db import models
from django.contrib.auth.models import User


class User(User):
    friends = models.ManyToManyField(User, related_name='friends')

    def get_friends(self):
        return ",".join([str(p) for p in self.friends.all()])