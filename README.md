
# AI-Powered Stock Trading Program

## Overview
This AI-powered stock trading program automates the process of trading stocks by leveraging the capabilities of OpenAI's GPT-4 model. The program operates in several stages:
1. It begins by fetching the latest news in the tech sector from two sources: Bing and Newsdata.io APIs.
2. Using a two-step prompt engineering approach, the program then analyzes these headlines with OpenAI's GPT-4. In the first step, GPT-4 generates general stock market trends and predictions based on the given news headlines. In the second step, it delivers specific buy or sell recommendations for stocks. These recommendations are provided in a structured JSON format, ensuring consistency and ease of interpretation. This format includes details such as the stock symbol, the recommended action (buy or sell), and a confidence metric.
3. Finally, the program uses the Alpaca Trading API to execute trades based on these AI-generated predictions and recommendations.

This streamlined process aims to provide an advanced, AI-driven approach to stock trading, potentially offering insights beyond conventional analysis by considering broader market impacts and interconnections implied by the latest news.

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Dependencies
To install the required Python packages, run the following command:
```bash
pip install requests openai alpaca_trade_api
```

### API Keys
You will need to obtain API keys from:
- Bing News Search API
- Newsdata.io
- OpenAI
- Alpaca Trading API

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yuenler/trader.git
   ```
2. Enter the directory:
   ```bash
   cd trader
   ```

Before running the program, create a `.env` file in the root directory with the following variables:
- `BING_API_KEY`: Your Bing News Search API key.
- `NEWSDATA_API_KEY`: Your Newsdata.io API key.
- `OPENAI_API_KEY`: Your OpenAI API key.
- `ALPACA_API_KEY`: Your Alpaca Trading API key.
- `ALPACA_SECRET_KEY`: Your Alpaca Trading secret key.


## Usage
Run the `main.py` script to start the program:
```bash
python main.py
```
The program will continuously fetch news, analyze it, and execute trades every 15 minutes.

## Configuration
- You can adjust the frequency of the trading loop by modifying the sleep interval in `main.py`.
- Update the query parameters in `news_bing.py` and `news_newsdata.py` to change the news sources or topics.

