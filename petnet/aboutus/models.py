from django.db import models


class Aboutus(models.Model):
    email = models.EmailField(max_length=500, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Phone')
    address = models.CharField(max_length=100, verbose_name='Address')