from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('reservations.urls', 'reservations'), namespace='reservations')),
    path('admin/', admin.site.urls),
]
