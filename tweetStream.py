# author: anuvabh
import twitter
import json
import os

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

def fetch(api, file):

# for tweet in streamSample:
# 	if tweet.get('lang') == 'en':
# 		print tweet['id'] , " : " ,tweet.get('text')	

	data = {}
	streamSample = api.GetStreamFilter(track="QQCCMH8")
	for tweet in streamSample:
		if tweet.get('lang') == 'en' and tweet.get('text') and tweet.get('geo'):
			data['tweet_id'] = str(tweet['id'])
			data['text'] = tweet.get('text')
			data['geo'] = tweet.get('geo')
			json.dump(data, file)			
			file.write(",")

def search(api, file):
	results = api.GetSearch(term="#QQCCMH8", count=200)
	data = {}
	for tweet in results:		
		if tweet.lang == 'en' and tweet.text:
			data['tweet_id'] = str(tweet.id)
			# data['user'] = tweet.user.get('screen_name')
			data['text'] = tweet.text
			json.dump(data, file)			
			file.write(",")			

# add command line params
try:
	file = open('geotweets2.txt', 'w')
	file.write("[")
	fetch(api, file)
	file.seek(-1, os.SEEK_END)
	file.write("]")
	file.close()
except:
	print "error"
	file.seek(-1, os.SEEK_END)
	file.write("]")
	file.close()

# print api.GetStatus(570175478784356352).user.screen_name