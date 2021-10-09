from django.core.mail import send_mail
from django.conf import settings

SUBJECT = 'PetNet Welcome email!'
MESSAGE_BODY = 'Hello, {name}. Welcome to the PetNet.'


class EmailService:
    def __init__(self, user):
        self.user = user

    def send(self):
        name = self.user.first_name or self.user.email
        send_mail(SUBJECT, MESSAGE_BODY.format(name=name), settings.EMAIL_HOST_USER, [self.user.email], fail_silently=False)