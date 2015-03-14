# author: anuvabh
import twitter
import json
import os
import time
  
def fetch(api, file):
	
	data = {}
	streamSample = api.GetStreamSample()
	for tweet in streamSample:
		if tweet.get('lang') == 'en' and tweet.get('text') and tweet.get('geo'):
			data['tweet_id'] = str(tweet['id'])
			data['text'] = tweet.get('text')
			data['geo'] = tweet.get('geo')
			json.dump(data, file)			
			file.write(",")

def search(api, file, query):
	results = api.GetSearch(term = query, count = 100)
	data = {}
	since_id = 0

	for i in range(1, 500):
		
		for tweet in results:		
			if tweet.lang == 'en' and tweet.text:
				data['tweet_id'] = str(tweet.id)
				# data['user'] = tweet.user.get('screen_name')
				data['text'] = tweet.text
				json.dump(data, file)			
				file.write(",")

			since_id = max(since_id, data['tweet_id'])

		print since_id
		results = api.GetSearch(term = query, count = 100, since_id = since_id, result_type='recent')

# add command line params

data = open('keys/vabh.txt').read().splitlines()

api = twitter.Api(consumer_key=data[0],
                  consumer_secret=data[1],
                  access_token_key=data[2],
                  access_token_secret=data[3])
try:
	timestr = time.strftime("%Y%m%d-%H%M%S") + '.txt'
	file = open("tweets/" + timestr, 'w')
	file.write("[")

	search(api, file, "Happy Pi Day")

	file.seek(-1, os.SEEK_END)
	file.write("]")
	file.close()
except:
	print "error"
	file.seek(-1, os.SEEK_END)
	file.write("]")
	file.close()

# print api.GetStatus().user.screen_name