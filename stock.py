import requests
import html
from twilio.rest import Client
url = 'https://www.alphavantage.co/query'
new_api = "https://newsapi.org/v2/everything https://newsapi.org"
api_for_news = "pate your own api key from "
req_parms = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":"IBM",
    "apikey":"get your own api key from https://www.alphavantage.co"
}

req_to_api = requests.get(url,req_parms)
data = req_to_api.json()
print(data)
new_data = data["Time Series (Daily)"]
new_list = [value for key,value in new_data.items()]
yesterday_data = new_list[0]
yesterday_closing = yesterday_data['4. close']
p=float(yesterday_closing)
yesterday_before_data = new_list[1]
yesterday_before_closing = yesterday_before_data['4. close']
q=float(yesterday_before_closing)
z = round(p-q,2)
sign = ""
if z >0:
    sign = "🔺"
else:
    sign = "🔻"
total_per =(round(p-q,2)/q)*100
print(total_per)
if total_per > 1:
    account_sid = "get sid from twilio"
    auth_token = "also this from twilio"
    news_prams = {
        "apikey":api_for_news,
        "qInTitle":"IBM"
    }
    news_request = requests.get(new_api,news_prams)
    news_json = news_request.json()["articles"]
    three_t=news_json[:3]
    item_list = [f"IBM {sign}{total_per}%\nHeadlines : {html.escape(i['title'])}.\n Description : {html.escape(i['description'])}" for i in three_t]


    client = Client(account_sid, auth_token)
    for j in item_list:
        message = client.messages.create(
            body="ka ho kareja",
            from_='+13613211019',
            to='+91your mobile no'
        )

        print(message.sid)
