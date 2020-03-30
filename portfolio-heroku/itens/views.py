from django.shortcuts import render
from django.template.defaulttags import register
import json
import requests


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# Create your views here.
def list_item(request):
    json_ = requests.get('http://ddragon.leagueoflegends.com/cdn/10.6.1/data/pt_BR/item.json').json()
        
    image = 'http://ddragon.leagueoflegends.com/cdn/10.6.1/img/item/'
    index = []
    for i in json_['data']:
        index.append(json_['data'][i])

    data = {'data': json_['data'], 'image': image, 'index': index, }
    return render(request, 'list_item.html', data)
