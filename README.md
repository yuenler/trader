
# AI-Powered Stock Trading Program

## Overview
This program is designed to automate stock trading by parsing news headlines using OpenAI's GPT-4 model. It fetches recent news from the tech sector using Bing and Newsdata.io APIs, analyzes the headlines with OpenAI to predict stock market trends, and executes trades using the Alpaca Trading API.

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

