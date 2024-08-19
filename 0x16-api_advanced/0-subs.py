#!/usr/bin/python3
"""This module contains the function `number_of_subscribers(subreddit)`"""
import requests


def number_of_subscribers(subreddit):
    """
    This function  returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": 'Google Chrome Version 81.0.4044.129'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Extract the number of subscribers
        return data.get('data', {}).get('subscribers', 0)

    return 0
