import alpaca_trade_api as tradeapi
import os
import json
from dotenv import load_dotenv

load_dotenv()

def calculate_quantity(api, investment_amount, current_price):
    quantity = investment_amount / current_price

    # check time, if it's not a day order round to nearest whole number to avoid fractional shares
    time = api.get_clock().timestamp
    # Adjusting for typical market hours of 9:30 AM to 4:00 PM
    if 9 <= time.hour < 16:
        if time.hour == 9 and time.minute < 30:
            quantity = round(quantity)  # Round to whole number before 9:30 AM
        else:
            quantity = round(quantity, 2)  # Round to two decimal places during market hours
    else:
        quantity = round(quantity)
    
    return quantity

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

        current_price = api.get_latest_trade(stock).price

        if action == 'buy':
            if confidence == 'high':
                investment_amount = 2000
                quantity = calculate_quantity(api, investment_amount, current_price)

                print(f"Buying {quantity} shares of {stock} for ${quantity * current_price}.")
               
                # Submit the order
                try:
                    api.submit_order(
                        symbol=stock, 
                        qty=quantity, 
                        side='buy', 
                        type='market', 
                        time_in_force='gtc'
                    )
                except:
                    print(f'Error occurred when buying {stock}.')
                    print(e)

            else:
                investment_amount = 1000
                quantity = calculate_quantity(api, investment_amount, current_price)

                print(f"Buying {quantity} shares of {stock} for ${quantity * current_price}.")

                # Submit the order
                try:
                    api.submit_order(
                        symbol=stock, 
                        qty=quantity,  
                        side='buy', 
                        type='market', 
                        time_in_force='gtc'
                    )
                except Exception as e:
                    print(f'\nError occurred when buying {stock}.')
                    print(e)

                

