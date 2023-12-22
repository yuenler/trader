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
    
    user_prompt = (
        f"I have a list of news headlines and require your help to filter them. My sole interest lies in identifying " \
        f"headlines that pertain to novel breaking news with potential stock market impact. Please sift through the headlines " \
        f"and exclude any that are reactionary or interpretive of past events, or those aimed at consumer advice, like what to buy. " \
        f"I need only the list of headlines that meet these specific criteria. If none of the headlines are relevant in this context, " \
        f"simply state that there are no applicable headlines. Do not provide any additional information or analysis. " \
        f"\n\nOriginal NEWS HEADLINES:\n{combined_headlines}"
    )

    response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=[
          {'role': 'user', 'content': user_prompt},
      ],
      seed=seed,
    )

    filtered_headlines = response.choices[0].message.content


    follow_up_prompt = (
        f"Given this list of headlines, please predict how they will affect the news will affect stock market " \
        f"Please go beyond just the companies mentioned in the headlines. Consider factors like the industries " \
        f"these companies depend on and the companies that invest in them. Provide me with a list of stocks, " \
        f"along with a very short and concise prediction for each of them." \
        f"\n\ NEWS HEADLINES:\n{filtered_headlines}"
    )

    response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=[
          {'role': 'user', 'content': follow_up_prompt},
      ],
      seed=seed,
    )


    general_trends = response.choices[0].message.content

    # Second prompt to get buy/sell recommendations in a specific JSON format
    follow_up_prompt_2 = f"Based on your analysis, can you provide buy/sell recommendations for each stock. This is for short term trading, so don't tell me to hold. " \
                       f"you mentioned in a JSON format? Also indicate each prediction as high/low confidence. The JSON should have the format: " \
                       f"{{'stock_symbol': {{'action': 'buy/sell', 'confidence': high/low}}}}."

    response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      response_format={ "type": "json_object" },
      messages=[
          {'role': 'user', 'content': follow_up_prompt},
          {'role': 'assistant', 'content': general_trends},
          {'role': 'user', 'content': follow_up_prompt_2},
      ],
      seed=seed,
    )

    recommendations_json = response.choices[0].message.content

    print('\nGiven the above news headlines, GPT-4 finds that the following headlines are relevant:\n')
    print(filtered_headlines)
    print('\nGiven these relevant headlines, GPT-4 finds the following general trends:\n')
    print(general_trends)
    print('\nGiven these predicted trends, GPT-4 recommends the following trades:\n')
    print(recommendations_json)

    return recommendations_json
