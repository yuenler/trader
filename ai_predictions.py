import openai
import os
from dotenv import load_dotenv

load_dotenv()

def get_ai_predictions(news_headlines):
    """
    Sends news headlines to OpenAI and gets specific buy/sell recommendations in a predefined JSON format.
    Input: List of tuples (headline, datePublished).
    Returns: JSON string containing buy/sell recommendations for each stock and confidence metric.
    """
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # First prompt to get general stock trends
    combined_headlines = '. '.join([headline for headline, _ in news_headlines])
    initial_prompt = f"I'm going to give you news headlines and you will tell me what stocks to buy. " \
                     f"Consider the industries these companies depend on and the companies that invest in " \
                     f"them. Give me a list of stocks and a short prediction for each of them.\n\n" \
                     f"NEWS DATA:\n{combined_headlines}"

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=initial_prompt,
      max_tokens=250
    )

    general_trends = response.choices[0].text.strip()

    # Second prompt to get buy/sell recommendations in a specific JSON format
    follow_up_prompt = f"Based on the previous analysis, provide buy/sell recommendations for each stock " \
                       f"mentioned in a JSON format. The JSON should have the format: " \
                       f"{{'stock_symbol': {{'action': 'buy/sell', 'confidence': percentage}}}}."

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=follow_up_prompt,
      max_tokens=250
    )

    recommendations_json = response.choices[0].text.strip()

    return recommendations_json
