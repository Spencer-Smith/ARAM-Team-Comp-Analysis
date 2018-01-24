import requests
from sys import exit
from json import loads
from time import sleep

# Example request:
#r = requests.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/RiotSchmick?api_key=xxxxx-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')

APIkey = open(apikey.txt,'r').readline().strip()
URL = 'https://na1.api.riotgames.com'
account = '/lol/summoner/v3/summoners/by-name/'
matchlist = '/lol/match/v3/matchlists/by-account/'
champions = '/lol/static-data/v3/champions'
match = '/lol/match/v3/matches/'
aram_queue = 'queue=450'
season = 'season=9'

def getAccountId(summonerName):
    request = URL + account + summonerName + '?' + APIkey
    data = makeRequest(request)
    return data['accountId']

def getRecentArams(accountId):
    request = URL + matchlist + str(accountId) + '?' + APIkey
    request += '&' + aram_queue + '&' + season
    data = makeRequest(request)
    return data['matches']

def getMatchData(matchId):
    request = URL + match + str(matchId) + '?' + APIkey
    data = makeRequest(request)
    return data

def getChampionData():
    request = URL + champions + '?' + APIkey
    data = makeRequest(request)
    return data['data']

def makeRequest(request):
    while True:
        print request
        r = requests.get(request)
        if r.status_code == 429:
            wait = r.headers['Retry-After']
            print "Rate limit reached. Sleeping %s seconds."%wait
            sleep(float(wait))
        elif not r.ok:
            print "Error: " + str(r.status_code)
            exit(1)
        else:
            data = loads(r.text)
            return data
