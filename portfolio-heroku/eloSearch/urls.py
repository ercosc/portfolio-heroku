from django.contrib import admin
from django.urls import path
from .views import get_summoner, summoner_form

app_name = 'lol'
urlpatterns = [
    path('', summoner_form, name='form'),
    path('search/', get_summoner, name='get')
]
