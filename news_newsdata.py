import requests

def get_news_from_newsdata():
    url = "https://newsdata.io/api/1/news"
    params = {
        'apikey': 'YOUR_NEWSDATA_API_KEY',
        'q': 'technology',
        'language': 'en',
        'sortby': 'date'
    }
    response = requests.get(url, params=params)
    news_data = response.json()
    news_headlines = [(item['title'], item['pubDate']) for item in news_data['results']]
    return news_headlines
