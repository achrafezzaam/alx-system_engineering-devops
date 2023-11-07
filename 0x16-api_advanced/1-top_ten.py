#!/usr/bin/python3
''' Print the titles of the first 10 hot posts '''
import requests


def top_ten(subreddit):
    ''' Query the Reddit API and prints the titles of the first
        10 hot posts listed for a given subreddit '''
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 10}
    headers = {"User-Agent": "4ZfPk/maXs5rww=="}
    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    results = res.json()
    [print(item["data"]["title"]) for item in results["data"]["children"]]
