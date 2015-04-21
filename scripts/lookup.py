# author: anuvabh
import twitter
import json
import os
import time
import pprint
  
data = open('../keys/nastya.txt').read().splitlines()

api = twitter.Api(consumer_key=data[0],
                  consumer_secret=data[1],
                  access_token_key=data[2],
                  access_token_secret=data[3])

limit = api.GetRateLimitStatus()

timestr = time.strftime("search-%Y%m%d-%H%M%S") + '.txt'

query = "#Hillary2016"
# r = api.GetRateLimitStatus()
# pprint.pprint(r)
file = open("../tweets/" + query + timestr, 'w')

f_max = open("../tweets/max", 'r')
max_id = f_max.readline()
f_max.close()

choice = 1

if choice == 1: 
	# results = api.GetSearch(term = query, count = 100, lang = 'en', result_type = 'recent')
	while 1:
		try:
			limit = api.GetRateLimitStatus()
			remaining = limit['resources']['search']['/search/tweets']['remaining']
			print remaining
			print "max"
			if remaining != 0:
				results = api.GetSearch(term = query, count = 100, max_id = max_id, lang = 'en', result_type = 'recent')				
				for tweet in results:				
					# print tweet.id
					file.write(str(tweet))
					file.write("\n")
					max_id = min(max_id, tweet.id)
			max_id = max_id - 1
			print max_id
					
		except KeyboardInterrupt:
			file.close()
	 
			f1 = open('../tweets/max', 'w')
			# f1.seek(0)
			f1.write(str(max_id) + '\n')
			f1.close()
			break
		except twitter.error.TwitterError:
			print "error"
			break
		except:
			continue

else:
	# since
	while 1:
		try:
			limit = api.GetRateLimitStatus()
			remaining = limit['resources']['search']['/search/tweets']['remaining']
			print remaining
			print "since"

			if remaining != 0:
				results = api.GetSearch(term = query, count = 100, since_id = max_id, lang = 'en')				
				for tweet in results:				
					# print tweet.id
					file.write(str(tweet))
					file.write("\n")
					max_id = max(max_id, tweet.id)
			print max_id
					
		except KeyboardInterrupt:
			file.close()
	 
			f1 = open('../tweets/max', 'w')
			# f1.seek(0)
			f1.write(str(max_id) + '\n')
			f1.close()
			break
		except twitter.error.TwitterError:
			print "error"
			break
		except:
			continue