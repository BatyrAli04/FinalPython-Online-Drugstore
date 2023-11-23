from django.urls import path

from fav import views

app_name = 'fav'

urlpatterns = [
    path('', views.view_fav, name='favs',),
]