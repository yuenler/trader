import time
from news_bing import get_news_from_bing
from news_newsdata import get_news_from_newsdata
from ai_predictions import get_ai_predictions
from execute_trades import execute_trades

def main(num_minutes_between_runs):
    # set last checked to yesterday
    is_first_run_of_day = True

    while True:
        # Get news headlines
        newsdata_news = get_news_from_newsdata(is_first_run_of_day, num_minutes_between_runs)
        
        # bing_news = get_news_from_bing(is_first_run_of_day, num_minutes_between_runs)
        bing_news = []

        # Combine news sources
        all_news = bing_news + newsdata_news

        # Print all news in a formatted way
        for news in all_news:
            print(f"{news[1]}: {news[0]}\n")


        # Get AI predictions
        json_predictions = get_ai_predictions(all_news)

        # Execute trades
        execute_trades(json_predictions)

        is_first_run_of_day = False

        # Wait for 15 minutes
        time.sleep(num_minutes_between_runs * 60)

if __name__ == "__main__":
    NUM_MINUTES_BETWEEN_RUNS = 15
    main(NUM_MINUTES_BETWEEN_RUNS)
