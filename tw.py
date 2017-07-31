from requests_oauthlib import OAuth1Session

import config


def tweet(status):
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    twitter = OAuth1Session(config.CK, config.CS, config.AT, config.AS)
    params = {'status': status}
    req = twitter.post(url, params=params)

    if(req.status_code == 200):
        print('Tweeted')
    else:
        print('Tweet Error ' + str(req.status_code))
