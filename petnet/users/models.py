from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    friends = models.ManyToManyField(User, related_name='friends')
    about = models.CharField(max_length=500, verbose_name='About')
    phone = models.CharField(max_length=25, verbose_name='Phone')
    address = models.CharField(max_length=100, verbose_name='Address')
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    
    def get_friends(self):
        return ",".join([str(p) for p in self.friends.all()])

