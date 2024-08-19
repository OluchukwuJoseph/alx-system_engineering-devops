#!/usr/bin/python3
"""This module contains the function `top_ten(subreddit)`"""
import requests


def top_ten(subreddit):
    """
    This function queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    # Check for valid HTTP response
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')
        if posts:
            for post in posts:
                print(post.get('data').get('title'))

    print(None)
