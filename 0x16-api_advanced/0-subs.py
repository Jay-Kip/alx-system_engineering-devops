#!/usr/bin/python3
"""
Returns Number of subscribers from reddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """Function that querries reddit API and returns
    number of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    user_agent = {'User-agent': 'google Chrome Version 81.0.4044.129'}
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return resulrs.get('data').get('subscribers')
    
    except Exception:
        return 0