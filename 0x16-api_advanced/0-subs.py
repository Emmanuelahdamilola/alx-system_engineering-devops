import requests

def number_of_subscribers(subreddit):
    user_agent = '0x16-api_advanced-luna'
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    headers = {'User-Agent': user_agent}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()['data']
        page_data = data['children'][0]['data']
        return page_data['subreddit_subscribers']
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except (KeyError, ValueError) as e:
        print(f"Error parsing JSON: {e}")

    return 0
