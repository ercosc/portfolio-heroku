from django.urls import path
from .views import champions, champ_by_name

app_name = 'champ'
urlpatterns = [
    path('', champions, name='all'),
    path('<slug:slug>', champ_by_name, name='name')
]