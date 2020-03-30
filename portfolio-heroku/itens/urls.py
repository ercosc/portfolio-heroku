from django.urls import path
from .views import list_item


app_name = 'item'
urlpatterns = [
    path('', list_item, name='list')
]
