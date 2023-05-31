from newsapi import NewsApiClient
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "XV35ESFZQO2CRWSV"


stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY

}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = (difference/float(yesterday_closing_price)) * 100
print(diff_percent)

if diff_percent > 2:
    NEWS_API_KEY = 'c406732bda7f40cf97758da670e33f9a'
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "language": "en"
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()["articles"][:3]
    formatted_articles_list = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline:{article['title']}\nBrief:{article['description']}" for article in news_data]

    account_sid = "ACf8df2bd539864704fcd245888b3fd5d1"
    auth_token = "a39bd4d0e95e1230435f38d15bb02388"
    client = Client(account_sid, auth_token)

    for article in formatted_articles_list:
        message = client.messages.create(
                body=article,
                from_='+15075744225',
                to='+919818996367'
            )
        print(message.status)
