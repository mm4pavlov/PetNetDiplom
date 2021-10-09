from django.urls import include, path
from rest_framework import routers
from . import views
from .views import CurrentUserView


router = routers.DefaultRouter()
router.register(r'news', views.UsersPost)

urlpatterns = [
    path('posts/', include(router.urls)),
    path('users', CurrentUserView.as_view())
]
