import openai
import os
from dotenv import load_dotenv

load_dotenv()

def get_ai_predictions(news_headlines):
    """
    Sends news headlines to OpenAI and gets stock market predictions.
    Input: List of tuples (headline, datePublished).
    Returns: String containing AI's predictions.
    """
    openai.api_key = os.getenv('OPENAI_API_KEY')

    combined_headlines = '. '.join([headline for headline, _ in news_headlines])

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"Given these news headlines: {combined_headlines}, what are the stock market predictions?",
      max_tokens=150
    )

    return response.choices[0].text.strip()
