#!/usr/bin/python3
"""Query Reddit API to count keyword occurrences in subreddit titles
"""

import requests


def count_keywords_in_titles(subreddit, keywords, count_list=[], next_page=None):
    """Recursively fetch subreddit titles and count keyword occurrences
    """
    # Convert keywords list to a dictionary with counts
    if not count_list:
        count_list = [{'keyword': keyword, 'count': 0} for keyword in keywords]

    # Networking
    # Set custom user-agent
    user_agent = '0x16-api_advanced-emma'
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    
    # If next_page specified, pass it as a parameter
    if next_page:
        url += f'?after={next_page}'

    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    # Data Parsing
    # Load response unit from JSON
    data = response.json()['data']

    # Extract list of posts
    posts = data['children']
    for post in posts:
        title = post['data']['title']
        for item in count_list:
            title_lower = title.lower()
            title_list = title_lower.split()
            item['count'] += title_list.count(item['keyword'].lower())

    next_page = data['after']
    if next_page is not None:
        return count_keywords_in_titles(subreddit, keywords, count_list, next_page)
    else:
        # Sort list by count
        sorted_list = sorted(count_list, key=lambda word: (word['count'], word['keyword']), reverse=True)
        keywords_matched = 0
        # Print keywords and counts
        for word in sorted_list:
            if word['count'] > 0:
                print('{}: {}'.format(word['keyword'], word['count']))
                keywords_matched += 1
        return
