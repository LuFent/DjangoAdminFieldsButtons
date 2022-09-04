from .views import *
from django.urls import path

app_name = 'adminbuttons'

urlpatterns = [
    path('send_message/', catch_button)
    ]
