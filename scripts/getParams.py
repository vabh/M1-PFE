import json
import pprint
import os
import glob
import bz2

tweets_path = '../tweets/iphone/'

os.chdir(tweets_path)
file_list = []
for f in glob.glob("*.txt.bz2"):
    file_list.append(f)
os.chdir('../../scripts')

out_file_name = 'iphone_data.txt'

proccessed_ids = {}
count = 0
with open(out_file_name, 'w') as f_out:
    for json_file in file_list:

        file_name = tweets_path + json_file

        # with open(file_name, 'r') as f:
        with bz2.BZ2File(file_name, 'rb') as f:
            for line in f:
                try:
                    l = json.loads(line)
                except:
                    print file_name
                    continue

                if l['id'] in proccessed_ids:
                    print "seen"
                    continue

                count += 1
                proccessed_ids[l['id']] = 1
                data = {}
                data['time'] = l['created_at'].split()[3]
                data['day'] = l['created_at'].split()[2]
                data['month'] = l['created_at'].split()[1]
                data['id'] = l['id']
                data['user'] = l['user']['screen_name']

                if 'user_mentions' in l:
                    user_mentions = l['user_mentions']
                    # print user_mentions
                    data['mentioned_user'] = []
                    for name in user_mentions:
                        data['mentioned_user'].append(name['screen_name'])
                    # print data['mentioned_user']

                if 'hashtags' in l:
                    data['hashtags'] = l['hashtags']

                if 'followers_count' in l['user']:
                    data['user_followers'] = l['user']['followers_count']
                else:
                    # -1 indicates follower count is not public
                    data['user_followers'] = -1

                # data['retweeted'] = l['retweeted']
                if 'retweeted_status' in l:
                    data['retweeted_status_id'] = l['retweeted_status']['id']
                    data['retweet_count'] = l['retweet_count']
                else:
                    data['retweeted_status_id'] = -1
                    data['retweet_count'] = -1

                json.dump(data, f_out)
                f_out.write('\n')
        print file_name
            # print data
# pprint.pprint(data)
print count
