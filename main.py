import time
from news_bing import get_news_from_bing
from news_newsdata import get_news_from_newsdata
from ai_predictions import get_ai_predictions
from execute_trades import execute_trades

def main():
    while True:
        # Get news headlines
        bing_news = get_news_from_bing()
        newsdata_news = get_news_from_newsdata()

        # Combine news sources
        all_news = bing_news + newsdata_news

        # Get AI predictions
        general_trends, json_predictions = get_ai_predictions(all_news)

        # Execute trades
        execute_trades(json_predictions)

        print(general_trends)
        print('Given these predicted trends, GPT-4 recommends the following trades:')
        print(json_predictions)

        # Wait for 15 minutes
        time.sleep(900)

if __name__ == "__main__":
    main()
