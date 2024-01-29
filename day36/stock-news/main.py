
import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "YOUR API KEY"
NEWS_API_KEY = "YOUR API KEY"

TWILIO_SID ="YOUR API KEY"
TWILIO_AUTH = "YOUR API KEY"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
#print(response.json())

data = response.json()["Time Series (Daily)"]
#print(data)
data_list = [value for (key,value) in data.items()]
print(data_list)

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)
difference = abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
print(difference)

diff_per = (difference/float(yesterday_closing_price)) * 100
print(diff_per)

if diff_per > 0.2:  # change 0.2 to as you wish.. change in stock percentage

    news_params={
        "apiKey": NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}"for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_="+16592167197",
            to="+919458173369"
        )

