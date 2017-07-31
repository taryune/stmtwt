import json

import requests

import config


def getPlayerStatus(steamid):
    key = config.SteamAPIKey
    interface = 'ISteamUser'
    method = 'GetPlayerSummaries'
    version = 'v0002'
    formatType = 'json'

    url = 'http://api.steampowered.com/{interface}/{method}/{version}/?key={key}&steamids={steamid}'.format(
        **locals())

    result = requests.get(url).json()
    tmp = result['response']['players'][0]

    pstate = {}
    pstate['steamid'] = tmp.get('steamid')
    pstate['personaname'] = tmp.get('personaname')

    st = tmp.get('personastate')
    if(st == 0):
        pstate['personastate'] = 'Offline'
    elif(st == 1):
        pstate['personastate'] = 'Online'
    elif(st == 2):
        pstate['personastate'] = 'Busy'
    elif(st == 3):
        pstate['personastate'] = 'Away'
    elif(st == 4):
        pstate['personastate'] = 'Snooze'
    elif(st == 5):
        pstate['personastate'] = 'looking to trade'
    elif(st == 6):
        pstate['personastate'] = 'looking to play'

    pstate['gameid'] = tmp.get('gameid')
    pstate['gameextrainfo'] = tmp.get('gameextrainfo')
    pstate['lobbysteamid'] = tmp.get('lobbysteamid')

    return pstate


def genPlayerURL(steamid):
    if(steamid):
        return ('http://steamcommunity.com/profiles/' + str(steamid))


def genStoreURL(gameid):
    if(gameid):
        return ('http://store.steampowered.com/app/' + str(gameid))


def genJoinURL(gameid, lobbysteamid, steamid):
    if(lobbysteamid):
        return tiny_url('steam://joinloby/{gameid}/{lobbysteamid}/{steamid}'.format(**locals()))


def genPlayURL(gameid):
    if(gameid):
        return tiny_url('steam://run/{gameid}'.format(**locals()))


def tiny_url(lurl):
    url = 'http://tinyurl.com/api-create.php?url=' + lurl
    return requests.get(url).text
