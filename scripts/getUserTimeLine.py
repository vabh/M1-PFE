import twitter
import json
import traceback
import linecache

from dateTimetoEpoch import to_UnixTime

keys = open('../keys/vabh.txt').read().splitlines()
# keys = open('../keys/nastya.txt').read().splitlines()

api = twitter.Api(consumer_key=keys[0],
                  consumer_secret=keys[1],
                  access_token_key=keys[2],
                  access_token_secret=keys[3])
file_name = 'iphone-spam-user-list.txt'
# user_name = open(file_name, 'r').readline()

# number of lines in file, choose user randomly
with open(file_name, 'r') as f_usernames:

    # for i in range(60):
    #     f_usernames.readline()

    for i in range(90, 100):

        # user_name = f_usernames.readline().strip()
        user_name = linecache.getline(file_name, i + 1).strip()
        max_id = -1
        with open('spam_users_timeline/' + user_name + '.txt', 'w') as f_out:
            print user_name, i
            for j in range(0, 18):

                try:
                    if max_id == -1:
                        user_tweets = api.GetUserTimeline(
                            screen_name=user_name, count=100, include_rts=1)
                    else:
                        user_tweets = api.GetUserTimeline(
                            screen_name=user_name, max_id=max_id, count=100, include_rts=1)
                except Exception:
                    print(traceback.format_exc())
                    continue

                for tweet in user_tweets:
                    try:
                        tweet_data = json.loads(str(tweet))
                    except:
                        print 'error'
                        continue

                    if max_id == -1:
                        max_id = tweet_data['id']
                    else:
                        max_id = min(max_id, tweet_data['id']) - 1

                    data = {}
                    if 'hashtags' in tweet_data:
                        data['hashtags'] = tweet_data['hashtags']

                    data['created_at'] = tweet_data['created_at']

                    json.dump(data, f_out)
                    f_out.write('\n')

to_UnixTime()
# strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
