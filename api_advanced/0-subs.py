#!/usr/bin/python3
"""
This module provides a function for retrieving the number of subscribers for a given subreddit from Reddit's API.

The function defined in this module is:
    - number_of_subscribers(subreddit): Returns the number of subscribers for the given subreddit.

Example usage:
    >>> number_of_subscribers('python')
    2900000
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for the given subreddit.

    Parameters:
        subreddit (str): The name of the subreddit to retrieve subscriber count for.

    Returns:
        int: The number of subscribers for the given subreddit, or 0 if an error occurred.

    """
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
