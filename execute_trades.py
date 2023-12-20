import alpaca_trade_api as tradeapi
import os
import json
from dotenv import load_dotenv

load_dotenv()

def execute_trades(recommendations_json):
    """
    Executes trades using Alpaca Trading API based on AI recommendations.
    Input: JSON string containing AI's recommendations for buy/sell and confidence metric.
    """
    api = tradeapi.REST(os.getenv('ALPACA_API_KEY'), os.getenv('ALPACA_SECRET_KEY'), base_url='https://paper-api.alpaca.markets')

    # Parse the JSON recommendations
    try:
        recommendations = json.loads(recommendations_json)
    except json.JSONDecodeError:
        print("Failed to decode recommendations JSON.")
        return

    # Implement logic to execute trades based on recommendations
    for stock, details in recommendations.items():
        action = details.get("action")  # 'buy' or 'sell'
        confidence = details.get("confidence")

        # Placeholder for trade logic; customize based on your criteria
        print(f"Executing {action} for {stock} with confidence {confidence}.")
        # Example: api.submit_order(symbol=stock, qty=quantity, side=action, type='market', time_in_force='gtc')
