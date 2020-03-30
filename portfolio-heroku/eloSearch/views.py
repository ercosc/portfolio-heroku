from django.shortcuts import render
from .forms import SummonerForm
import requests


# Create your views here.
def summoner_form(request):
    return render(request, 'eloSearch/index.html', {'form': SummonerForm})


def get_summoner(request):
    summoner_data = get_summoner_json(request.POST['name'])
    print(summoner_data)
    try:
        ranked_data = get_ranked_json(summoner_data)
        return render(request, 'eloSearch/get_summoner.html', {'data': ranked_data})
    except Exception:
        return render(request, 'eloSearch/error_summoner.html', {'data': summoner_data})


def get_summoner_json(name):
    server = 'br1'
    api_key = 'RGAPI-88d42263-8023-4afa-b38e-962bb08ca478'
    url = 'https://' + server + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name + '?api_key=' + api_key

    return requests.get(url).json()


def get_ranked_json(summoner):
    server = 'br1'
    api_key = 'RGAPI-88d42263-8023-4afa-b38e-962bb08ca478'
    id = summoner['id']
    url = 'https://' + server + '.api.riotgames.com/lol/league/v4/entries/by-summoner/' + id + '?api_key=' + api_key

    return requests.get(url).json()[0]


def get_error_json(error):
    return error['status']
