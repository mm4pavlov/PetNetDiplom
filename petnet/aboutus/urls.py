from django.urls import path
from .views import AboutusView

urlpatterns = [
    path('', AboutusView.as_view())
]