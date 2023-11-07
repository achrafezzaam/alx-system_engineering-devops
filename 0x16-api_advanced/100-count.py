#!/usr/bin/python3
''' Parse the title of all hot articles,
    and prints a sorted count of given keywords '''
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    ''' Recursive function that queries the Reddit API,
        parses the title of all hot articles,
        and prints a sorted count of given keywords  '''
    url = 'http://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                after)
    headers = {'User-agent': '4ZfPk/maXs5rww=='}
    res = requests.get(url, headers=headers)
    if after is None:
        word_list = [word.lower() for word in word_list]
    if res.status_code == 200:
        res = res.json()
        after = res['data']['after']
        for item in res['data']['children']:
            title = item['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if after is not None:
            count_words(subreddit, word_list, found_list, after)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, val in sorted(result.items(), key=lambda item: item[1],
                                   reverse=True):
                print('{}: {}'.format(key, val))
    else:
        return
