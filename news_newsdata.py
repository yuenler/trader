import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_news_from_newsdata():
    """
    Fetches the latest news from newsdata.io.
    Returns: List of tuples (title, pubDate).
    """
    url = "https://newsdata.io/api/1/news"
    params = {
        'apikey': os.getenv('NEWSDATA_API_KEY'),
        'q': 'technology',
        'language': 'en',
        'sortby': 'date'
    }
    response = requests.get(url, params=params)
    news_data = response.json()
    news_headlines = [(item['title'], item['pubDate']) for item in news_data['results']]
    return news_headlines
