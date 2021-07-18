import csv
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime
import os

today = datetime.now()

dir = "".join(today.strftime('%Y%m%d'))
os.mkdir("scrapedData/" + dir)

finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['AMZN', 'GOOG', 'FB','RS','HDB','INFY','RDY','TTM','AZRE']

news_tables = {}
for ticker in tickers:
    url = finviz_url + ticker

    req = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(req)

    html = BeautifulSoup(response, features='html.parser')
    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table

    parsed_data = []

    for ticker_value, news_table in news_tables.items():

        for row in news_table.findAll('tr'):

            title = row.a.text
            date_data = row.td.text.split(' ')
            if len(date_data) == 1:
                time = date_data[0]
            else:
                date = date_data[0]
                time = date_data[1]

            parsed_data.append([ticker_value,date,title])


    fields = ['Tiker', 'Date','Title']
    with open(f'./scrapedData/{dir}/{ticker}.csv', 'w',newline='') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(parsed_data)
    print(f"Done the scraping for {ticker} Date: {today.strftime('%Y%m%d')}")