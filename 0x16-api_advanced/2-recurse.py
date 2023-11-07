#!/usr/env/python3
''' List the titles of all hot articles for a given subreddit '''
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    ''' Recursive function that queries the Reddit API and
        returns a list containing the titles of all hot articles
        for a given subreddit '''
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "4ZfPk/maXs5rww=="}
    params = {"after": after, "count": count}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None
    results = res.json()
    after = results["data"]["after"]
    count += results["data"]["dist"]
    #for item in results["data"]["children"]:
    #    hot_list.append(item["data"]["title"])
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
