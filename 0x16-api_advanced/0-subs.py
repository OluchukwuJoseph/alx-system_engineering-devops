#!/usr/bin/python3
"""This module contains the function `number_of_subscribers(subreddit)`"""
import requests


def number_of_subscribers(subreddit):
    """
    This function  returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    headers = {'User-Agent': 'My User Agent'}

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        if response.text:
            data = response.json()

            subcribers_count = data['data']['subscribers']
            return subcribers_count

    return 0
