#!/usr/bin/python3
"""
This module provides functionality for retrieving the number of subscribers for a given subreddit on Reddit.

The main function provided by this module is number_of_subscribers(subreddit), which takes a subreddit name as input
and returns the number of subscribers for that subreddit as an integer.
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data['data']['subscribers']


if __name__ == "__main__":
    subreddit = "AskReddit"
    subscribers = number_of_subscribers(subreddit)
    print(f"{subreddit} has {subscribers} subscribers")
