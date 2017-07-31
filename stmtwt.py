import datetime
import time

import requests

import config
import steam
import tw

steamid = config.steamid

tmp_s = ''
st = ''
tmp = ''
tweet = ''

try:
    while True:
        ps = steam.getPlayerStatus(steamid)
        tmp_s = ps['personaname'] + ' is ' + ps['personastate']
        if(tmp_s != st):
            st = tmp_s
            print(st)

        if(ps['gameid']):
            tmp = ps['personaname'] + ' is playing ' + ps['gameextrainfo'] + '\n' + \
                steam.genStoreURL(ps['gameid']) + '\n' + \
                'Play! -> ' + steam.genPlayURL(ps['gameid'])
            if(ps['lobbysteamid']):
                tmp += '\nJoin! -> ' + \
                    steam.genJoinURL(
                        ps['gameid'], ps['lobbysteamid'], ps['steamid'])

        if(tmp != tweet):
            tweet = tmp
            print('tweet: ' + tweet)
            tw.tweet(datetime.datetime.today().strftime(
                "%Y/%m/%d %H:%M:%S") + '\n' + tweet)

        time.sleep(10)
except KeyboardInterrupt:
    print('\nOwari')
