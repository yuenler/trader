import requests

def get_news_from_bing():
    url = "https://api.bing.microsoft.com/v7.0/news/search"
    headers = {'Ocp-Apim-Subscription-Key': 'YOUR_BING_API_KEY'}
    params = {'q': 'tech sector', 'count': 10, 'sortBy': 'Date'}
    response = requests.get(url, headers=headers, params=params)
    news_data = response.json()
    news_headlines = [(item['name'], item['datePublished']) for item in news_data['value']]
    return news_headlines
