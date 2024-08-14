#!/usr/bin/python3
"""This module contains the function `number_of_subscribers(subreddit)`"""
import requests


def number_of_subscribers(subreddit):
    """
    This function  returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    url = f"https://reddit.com/r/{subreddit}/about.json"

    response = requests.get(url)
    # Check for valid HTTP response
    if response.status_code == 200:
        data = response.json()
        # Extract the number of subscribers
        return data.get('data', {}).get('subscribers', 0)
    else:
        # If the subreddit does not exist or other HTTP error, return 0
        return 0
