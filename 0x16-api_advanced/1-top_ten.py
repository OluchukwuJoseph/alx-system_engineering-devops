#!/usr/bin/python3
"""This module contains the function `top_ten(subreddit)`"""
import requests


def top_ten(subreddit):
    """
    This function queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
    """
    headers = {'User-Agent': 'My User Agent 1.0'}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    params = {"limit": 10}

    response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False
                )

    if response.status_code == 200:
        if response.text:
            data = response.json()
            results = data.get("data")

            for item in results.get("children"):
                title = item.get('data').get('title')
                print(title)
    else:
        print(None)
