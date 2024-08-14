#!/usr/bin/python3
"""Thi module contains the function `recurse(subreddit, hot_list=[])`"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API to retrieve all hot article titles
    for a given subreddit.

    Parameters:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list that accumulates the titles of hot articles.

    Returns:
        list: A list containing the titles of all hot articles for the given
        subreddit,
        or None if subreddit is invalid.
    """
    global after
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=headers,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
