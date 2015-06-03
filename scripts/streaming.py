# author: anuvabh
import twitter
import json
import os
import time
import pprint
import traceback
import sys
import bz2

# keys = open('../keys/vabh.txt').read().splitlines()
keys = open('../keys/nastya.txt').read().splitlines()

api = twitter.Api(consumer_key=keys[0],
                  consumer_secret=keys[1],
                  access_token_key=keys[2],
                  access_token_secret=keys[3])

while True:

    timestr = time.strftime("search-%Y%m%d-%H%M%S") + '.bz2'
    out_file_name = "../tweets/" + 'stream-' + timestr
    count = 0

    with bz2.BZ2File(out_file_name, 'wb', compresslevel = 9) as f_out:
        try:

            tweets = api.GetStreamSample()
            for tweet in tweets:

                if tweet.get('text') and tweet.get('lang') == 'en':
                    # print count, tweet.get('text')
                    # print count
                    count += 1
                    f_out.write(unicode(tweet))
                    # f_out.write(json.dumps(tweet))
                    f_out.write("\n")

                    if count > 1000:
                        print out_file_name
                        break

        except KeyboardInterrupt:
            sys.exit()
            break
        except twitter.error.TwitterError:
            print(traceback.format_exc())
            continue
        except:
            print(traceback.format_exc())
            # sys.exit()
            
