from django.shortcuts import render
from django.core import serializers
from .models import Champion
import requests
import json
from django.http import HttpResponse


# Create your views here.
def champions(request):
    a = requests.get('http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/champion.json').json()
    return render(request, 'champs/champ_search.html', {'data': a['data']})


def champ_by_name(request, slug):
    url = 'http://ddragon.leagueoflegends.com/cdn/10.6.1/data/pt_BR/champion/' + slug + '.json'
    champ_imgage = 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/'
    champ_passive = 'http://ddragon.leagueoflegends.com/cdn/10.6.1/img/passive/'
    champ_spells = 'http://ddragon.leagueoflegends.com/cdn/10.6.1/img/spell/'
    json_ = requests.get(url).json()

    data = {'data': json_['data'][slug], 'image': champ_imgage, 'passive': champ_passive, 'spells': champ_spells}
    return render(request, 'champs/champ_detail.html', data)
