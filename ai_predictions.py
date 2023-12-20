import openai

def get_ai_predictions(news_headlines):
    openai.api_key = 'YOUR_OPENAI_API_KEY'

    # Combine headlines into a single string
    combined_headlines = '. '.join([headline for headline, _ in news_headlines])

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"Given these news headlines: {combined_headlines}, what are the stock market predictions?",
      max_tokens=150
    )

    return response.choices[0].text.strip()
