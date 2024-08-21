'''#!/usr/bin/python3
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
        return 0'''

#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
                              v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs