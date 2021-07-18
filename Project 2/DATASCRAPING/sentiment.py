from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
def sentiment_scores(news):
	vader_obj = SentimentIntensityAnalyzer()
	sentiment_dict = vader_obj.polarity_scores(news)
	# decide sentiment as positive, negative and neutral
	if sentiment_dict['compound'] >= 0.05 :
		print(news,sentiment_dict['compound'],1)
	elif sentiment_dict['compound'] <= - 0.05 :
		print(news,sentiment_dict['compound'],-1)
	else :
		print(news,sentiment_dict['compound'],0)


# tickers = ['AMZN', 'GOOG', 'FB','RS','HDB','INFY','RDY','TTM','AZRE']
tickers = ['AMZN']
for i in tickers:
	with open(f'./scrapedData/{i}.csv', 'r') as f: # read csv file as a list of lists
		csv_reader = csv.reader(f) # pass the file object
		list_of_rows = list(csv_reader) # Pass reader object to list() to get a list of lists
		for i in list_of_rows:
			sentiment_scores(i[2])


    # with open(f'{ticker}.csv', 'w',newline='') as f:
    #     write = csv.writer(f)
    #     write.writerow(fields)
    #     write.writerows(i)

