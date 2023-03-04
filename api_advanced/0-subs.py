#!/usr/bin/python3
"""get number of subscribers function"""


import json
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    :param subreddit: The name of the subreddit to query.
    :return: The number of subscribers for the given subreddit, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # raise an exception if status code is not 200
        data = response.json()['data']
        return data['subscribers']
    except (requests.exceptions.HTTPError, json.JSONDecodeError):
        return 0


