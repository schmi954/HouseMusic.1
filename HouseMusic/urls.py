from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pollproject/', include('pollproject.urls')),
    path('admin/', admin.site.urls),
]