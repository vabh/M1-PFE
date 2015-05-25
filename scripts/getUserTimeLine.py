import twitter
import json

keys = open('../keys/nastya.txt').read().splitlines()

api = twitter.Api(consumer_key=keys[0],
                  consumer_secret=keys[1],
                  access_token_key=keys[2],
                  access_token_secret=keys[3])
file_name = 'iphone-spam-user-list.txt'
# user_name = open(file_name, 'r').readline()

# number of lines in file, choose user randomly
with open(file_name, 'r') as f_usernames:

    for i in range(0, 20):

        user_name = f_usernames.readline().strip()
        max_id = -1
        with open('spam_users_timeline/' + user_name + '.txt', 'w') as f_out:
            print user_name
            for j in range(0, 3):
                if max_id == -1:
                    user_tweets = api.GetUserTimeline(
                        screen_name=user_name, count=100, include_rts=1)
                else:
                    user_tweets = api.GetUserTimeline(
                        screen_name=user_name, max_id=max_id, count=100, include_rts=1)
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

                    data['created_at'] = tweet_data['created_at'].split()[3]
                    print data['created_at']
                    json.dump(data, f_out)
                    f_out.write('\n')
