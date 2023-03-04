#!/usr/bin/python3
"""
get hot articles function recursively
"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """
    Return a list containing the titles of all hot articles for a given subreddit.
    """
    if after == 'stop':
        return hot_list
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']
        children = data['children']
        after = data['after']
        for child in children:
            hot_list.append(child['data']['title'])
        return recurse(subreddit, hot_list, after)
    elif response.status_code == 404:
        return None
    else:
        return hot_list
