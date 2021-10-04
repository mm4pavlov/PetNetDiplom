from django.contrib import admin
from .models import Aboutus


class Aboutus(admin.ModelADmin):
    list_display = ['email', 'phone', 'address']


admin.site.register(Aboutus)
