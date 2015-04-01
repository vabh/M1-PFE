# author: anuvabh
import twitter
import json
import os
import time
  
def fetch(api, file, query):
	
	data = {}
	streamSample = api.GetStreamFilter(track='#ElClasico')	
	for tweet in streamSample:
		if tweet.get('text') and tweet.get('lang') == 'en':# and tweet.get('geo'):
			print tweet.get('text')
			data['tweet_id'] = str(tweet['id'])
			data['text'] = tweet.get('text')
			# data['geo'] = tweet.get('geo')
			json.dump(data, file)			
			file.write(",")

def search(api, file, query):
	data = {}

	since_id = 577963182813257728
	print ""
	for i in range(1, 500):
		results = api.GetSearch(term = query, count = 100, since_id = since_id, result_type = 'recent')

		for tweet in results:		
			if tweet.lang == 'en' and tweet.text:

				data['tweet_id'] = str(tweet.id)
				# data['user'] = tweet.user.get('screen_nam')
				if tweet.created_at:
					data['created_at'] = tweet.created_at
				data['text'] = tweet.text

				json.dump(data, file)			
				file.write(",")

				since_id = max(since_id, tweet.id)
				# add delay
		print since_id

def searchFull(api, file, query):
	data = {}

	since_id = 0
	
	for i in range(1, 500):

		results = api.GetSearch(term = query, count = 100, since_id = since_id, result_type = 'recent')
		for tweet in results:		
			if tweet.lang == 'en' and tweet.text:
				
				print tweet.text								
				file.write(tweet)
				file.write("\n")

				since_id = max(since_id, tweet.id)
		print since_id

def searchBack(api, file, query):
	data = {}

	max_id = 577069174331174912
	
	for i in range(1, 500):
		results = api.GetSearch(term = query, count = 100, until = '2015-03-15', max_id = max_id)

		for tweet in results:		
			if tweet.lang == 'en' and tweet.text:
				data['tweet_id'] = str(tweet.id)
				# data['user'] = tweet.user.get('screen_name')
				data['text'] = tweet.text
				json.dump(data, file)			
				file.write(",")

				max_id = min(max_id, data['tweet_id'])
				print data['tweet_id']
		# print max_id

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
	
	fetch(api, file, "#StPatricksDay")

	file.seek(-1, os.SEEK_END)
	file.write("]")
	file.close()
except:
	print "error"
	file.seek(-1, os.SEEK_END)
	file.write("]")
	file.close()

# print api.GetStatus().user.screen_name