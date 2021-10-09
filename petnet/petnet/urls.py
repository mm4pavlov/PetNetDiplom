from django.contrib import admin
from users.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('users.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
#    path('user/', CurrentUserView.as_view())
#    path('user/', include('users.urls')),
    path('contact/', include('contacts.urls')),
    path('aboutus/', include('aboutus.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
