from django.contrib import admin
from ..contacts.models import Contact
from ..aboutus.models import Aboutus

class Contact(admin.ModelADmin):
    list_display = ['email', 'phone', 'address']


admin.site.register(Contact)


class Aboutus(admin.ModelADmin):
    list_display = ['email', 'phone', 'address']


admin.site.register(Aboutus)