import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_API_KEY = os.getenv("AV_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def get_daily_data() -> dict:
    api_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": AV_API_KEY,
    }

    response = requests.get(api_url, params=params)
    return response.json()["Time Series (Daily)"]


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


def get_news():
    api_url = "https://newsapi.org/v2/everything"
    params = {
        "q": "tesla",
        "apiKey": NEWS_API_KEY,
        "pageSize": 3,
    }

    response = requests.get(api_url, params=params)
    return response.json()["articles"]


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


def send_sms(change, article):
    print(f"""
    {STOCK}: {"🔺" if change > 0 else "🔻"} {round(change, ndigits=2)}%
    Headline: {article["title"]}
    Brief: {article["description"]}
    """)


data = get_daily_data()
data = [value["4. close"] for (key, value) in data.items()]

yesterday_close = float(data[0])
day_before_close = float(data[1])
change_percentage = ((yesterday_close - day_before_close) / day_before_close) * 100

news_articles = get_news()
for news_article in news_articles:
    send_sms(change_percentage, news_article)
