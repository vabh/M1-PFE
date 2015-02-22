# author: anuvabh
import twitter
import json
import os

def fetch(api, file):

	streamSample = api.GetStreamSample()

	# for tweet in streamSample:
	# 	if tweet.get('lang') == 'en':
	# 		print tweet['id'] , " : " ,tweet.get('text')	
	data = {}
	for tweet in streamSample:
		if tweet.get('lang') == 'en' and tweet.get('text'):
			data['tweet_id'] = str(tweet['id'])
			data['text'] = tweet.get('text')
			json.dump(data, file)			
			file.write(",")

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')
try:
	file = open('tweet1.txt', 'w')
	file.write("[")
	fetch(api, file)
except:
	print "error"
	file.seek(-1, os.SEEK_END)
	file.write("]")
	file.close()