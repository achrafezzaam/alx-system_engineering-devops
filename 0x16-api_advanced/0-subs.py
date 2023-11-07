#!/usr/bin/python3
''' Gets the number of subscribers '''
import requests


def number_of_subscribers(subreddit):
    ''' Query the Reddit API and returns the number of subscribers
        for a given subreddit '''
    if subreddit is None or type(subreddit) is not str:
        return 0
    else:
        url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {"User-Agent": "4ZfPk/maXs5rww=="}
        res = requests.get(url, headers=headers).json()
        try:
            sub = res["data"]["subscribers"]
        except Exception as e:
            sub = 0
        return sub
