from django.urls import path

from reservations.views import IndexView

app_name = 'reservations'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]