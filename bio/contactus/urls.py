from django.urls import path

from .views import *

app_name = 'contactus'

urlpatterns = [
    path('', contactus, name='contactus'),
]