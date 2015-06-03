# author: anuvabh
import twitter
import json
import os
import time
import pprint

keys = open('../keys/vabh.txt').read().splitlines()
# keys = open('../keys/nastya.txt').read().splitlines()
current_key = 'nastya'


api = twitter.Api(consumer_key=keys[0],
                  consumer_secret=keys[1],
                  access_token_key=keys[2],
                  access_token_secret=keys[3])

limit = api.GetRateLimitStatus()

timestr = time.strftime("search-%Y%m%d-%H%M%S") + '.txt'

query = "#Hillary2016"
# r = api.GetRateLimitStatus()
# pprint.pprint(r)
out_file_id = open("../tweets/" + query + timestr, 'w')

# max_id = -1

f_max = open("../tweets/max", 'r')
max_id = f_max.readline()
f_max.close()

print max_id
choice = 1
if choice == 1:

    while 1:
        try:
            limit = api.GetRateLimitStatus()
            remaining = limit['resources']['search'][
                '/search/tweets']['remaining']
            print remaining
            print "max"
            if remaining != 0:

                if max_id == -1:
                    results = api.GetSearch(term = query, count = 100, lang = 'en', result_type = 'mixed')                    
                else:
                    results = api.GetSearch(term=query, count=100, max_id=max_id, lang='en', result_type='recent')
                
                for tweet in results:
                    # print tweet.id
                    out_file_id.write(str(tweet))
                    out_file_id.write("\n")
                    if max_id == -1:
                        max_id = tweet.id
                    else:
                        max_id = min(max_id, tweet.id)
            max_id = max_id - 1
            print max_id

        except KeyboardInterrupt:
            out_file_id.close()

            f1 = open('../tweets/max', 'w')
            # f1.seek(0)
            f1.write(str(max_id) + '\n')
            f1.close()
            break
        except twitter.error.TwitterError:

            print "error"
            if current_key == 'nastya':
                keys = open('../keys/vabh.txt').read().splitlines()
                current_key = 'vabh'
                api = twitter.Api(consumer_key=keys[0],
                                  consumer_secret=keys[1],
                                  access_token_key=keys[2],
                                  access_token_secret=keys[3])
                continue
            else:
                keys = open('../keys/nastya.txt').read().splitlines()
                current_key = 'nastya'
                api = twitter.Api(consumer_key=keys[0],
                                  consumer_secret=keys[1],
                                  access_token_key=keys[2],
                                  access_token_secret=keys[3])
                continue
        except:
            continue

else:
    # since
    while 1:
        try:
            limit = api.GetRateLimitStatus()
            remaining = limit['resources']['search'][
                '/search/tweets']['remaining']
            print remaining, current_key
            print "since"

            if remaining != 0:
                results = api.GetSearch(
                    term=query, count=100, since_id=max_id, lang='en')
                for tweet in results:
                    # print tweet.id
                    out_file_id.write(str(tweet))
                    out_file_id.write("\n")
                    max_id = max(max_id, tweet.id)
            print max_id

        except KeyboardInterrupt:
            out_file_id.close()

            f1 = open('../tweets/max', 'w')
            # f1.seek(0)
            f1.write(str(max_id) + '\n')
            f1.close()
            break
        except twitter.error.TwitterError:
            print "error"
            if current_key == 'nastya':
                keys = open('../keys/vabh.txt').read().splitlines()
                current_key = 'vabh'
                api = twitter.Api(consumer_key=keys[0],
                                  consumer_secret=keys[1],
                                  access_token_key=keys[2],
                                  access_token_secret=keys[3])
                continue
            else:
                keys = open('../keys/nastya.txt').read().splitlines()
                current_key = 'nastya'
                api = twitter.Api(consumer_key=keys[0],
                                  consumer_secret=keys[1],
                                  access_token_key=keys[2],
                                  access_token_secret=keys[3])
                continue
        except:
            continue
