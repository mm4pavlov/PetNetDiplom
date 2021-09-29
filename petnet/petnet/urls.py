from django.contrib import admin
from django.urls import path
from users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', CurrentUserView.as_view()),
]
