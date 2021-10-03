from django.contrib import admin
from django.urls import path, include, re_path




urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('user/', include('users.urls')),
    path('contact/', include('contacts.urls')),
    path('aboutus/', include('aboutus.urls')),
]
