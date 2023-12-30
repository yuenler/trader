import requests
import os
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.getenv('BING_API_KEY')
search_url = "https://api.bing.microsoft.com/v7.0/news/search"
headers = {"Ocp-Apim-Subscription-Key": subscription_key}

def get_news_from_bing(search_term):
    """
    Fetches the latest news from Bing News Search API.
    Returns: List of tuples (headline, datePublished).
    """
    params = {'q': search_term, 'count': 10, 'sortBy': 'Date'}
    response = requests.get(search_url, headers=headers, params=params)
    news_data = response.json()
    news_headlines = [(item['name'], item['datePublished']) for item in news_data['value']]
    # for x in news_headlines:
    #     print(x)
    return news_headlines

sample = get_news_from_bing('Microsoft')
print(sample)