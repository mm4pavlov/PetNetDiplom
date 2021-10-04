from django.contrib import admin
from .models import Contact

class Contact(admin.ModelADmin):
    list_display = ['email', 'phone', 'address']


admin.site.register(Contact)

