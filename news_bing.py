import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_news_from_bing():
    """
    Fetches the latest news from Bing News Search API.
    Returns: List of tuples (headline, datePublished).
    """
    url = "https://api.bing.microsoft.com/v7.0/news/search"
    headers = {'Ocp-Apim-Subscription-Key': os.getenv('BING_API_KEY')}
    params = {'q': 'tech sector', 'count': 10, 'sortBy': 'Date'}
    response = requests.get(url, headers=headers, params=params)
    news_data = response.json()
    news_headlines = [(item['name'], item['datePublished']) for item in news_data['value']]
    return news_headlines
