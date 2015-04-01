# author: anuvabh
import twitter
import json
import os
import time
import pprint
  
data = open('../keys/vabh.txt').read().splitlines()

api = twitter.Api(consumer_key=data[0],
                  consumer_secret=data[1],
                  access_token_key=data[2],
                  access_token_secret=data[3])

limit = api.GetRateLimitStatus()

timestr = time.strftime("search-%Y%m%d-%H%M%S") + '.txt'

query = "#ElClasico"
r = api.GetRateLimitStatus()
pprint.pprint(r)
# file = open("tweets/" + query + timestr, 'w')

# f_max = open("tweets/max", 'r')
# max_id = f_max.readline()
# f_max.close()

# # results = api.GetSearch(term = query, count = 100, lang = 'en', result_type = 'recent')
# while 1:
# 	try:
# 		limit = api.GetRateLimitStatus()
# 		remaining = limit['resources']['search']['/search/tweets']['remaining']
# 		print remaining

# 		if remaining != 0:
# 			results = api.GetSearch(term = query, count = 100, since_id = max_id, lang = 'en', result_type='recent')				
# 			for tweet in results:				
# 				print tweet.id
# 				file.write(str(tweet))
# 				file.write("\n")
# 				max_id = max(max_id, tweet.id)
# 		# print max_id
				
# 	except KeyboardInterrupt:
# 		file.close()
 
# 		file = open('tweets/max', 'w')		
# 		file.write(str(max_id) + "\n")
# 		file.close()
# 		break
# 	except:
# 		continue