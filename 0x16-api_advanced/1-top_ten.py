#!/usr/bin/python3
"""This module contains the function `top_ten(subreddit)`"""
import requests


def top_ten(subreddit):
    """
    This function queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check for valid HTTP response
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title', 'No title'))

    except Exception:
        # Handle any request exceptions and print None
        print(None)
