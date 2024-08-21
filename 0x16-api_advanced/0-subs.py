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
    
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)

    # Make get request
    response = get(url, headers=user_agent)

    # Check if response was successful
    if response.status_code != 200:
        return 0

    try:
        results = response.json() # Parse the response as JSON
        return results.get('data', {}).get('subscribers', 0) # Returns 0 if keys are missing
    
    except Exception:
        return 0