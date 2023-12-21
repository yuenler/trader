from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_ai_predictions(news_headlines):
    """
    Sends news headlines to OpenAI and gets specific buy/sell recommendations in a predefined JSON format.
    Input: List of tuples (headline, datePublished).
    Returns: JSON string containing buy/sell recommendations for each stock and confidence metric.
    """
    client = OpenAI()

    seed = 82

    # First prompt to get general stock trends
    combined_headlines = ' \n'.join([headline for headline, _ in news_headlines])
    system_prompt = f"The user will give you news headlines and you will tell them what stocks to buy. " \
                     f"Go beyond the companies mentioned in the headlines and consider factors like what" \
                     f"industries these companies depend on and the companies that invest in " \
                     f"them. Give them a list of stocks and a short prediction for each of them.\n\n" \

    response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=[
          {'role': 'system', 'content': system_prompt},
          {'role': 'user', 'content': combined_headlines},
      ],
      max_tokens=500,
      seed=seed,
    )

    general_trends = response['choices'][0]['message']['content']

    # Second prompt to get buy/sell recommendations in a specific JSON format
    follow_up_prompt = f"Based on your analysis, can you provide buy/sell recommendations for each stock " \
                       f"you mentioned in a JSON format? The JSON should have the format: " \
                       f"{{'stock_symbol': {{'action': 'buy/sell', 'confidence': percentage}}}}."

    response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      response_format={ "type": "json_object" },
      messages=[
          {'role': 'system', 'content': system_prompt},
          {'role': 'user', 'content': combined_headlines},
          {'role': 'assistant', 'content': general_trends},
          {'role': 'user', 'content': follow_up_prompt},
      ],
      max_tokens=200,
      seed=seed,
    )

    recommendations_json = response['choices'][0]['message']['content']

    return general_trends, recommendations_json
