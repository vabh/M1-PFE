import json
import pprint
import os
import glob
import bz2
import sys
import traceback
from time import mktime, strptime

tweets_path = '../tweets/stream/'
# tweets_path = ''

os.chdir(tweets_path)
file_list = []
for f in glob.glob("*.bz2"):
    file_list.append(f)
os.chdir('../../scripts/')

# print file_list
print len(file_list)

hashtags_processed = {}
hashtags_evolution = []
hash_count = 0
epoch_prev = 0
size_prev = 0
count = 0

for json_file in file_list:
    file_name = tweets_path + json_file
    count += 1
    # if count == 50:
    #     break
    with bz2.BZ2File(file_name, 'rb') as f:

        try:
            for line in f:
                try:
                    data = json.loads(json.dumps(eval(line)))

                    date_time = data['created_at']
                    pattern = '%a %b %d %H:%M:%S +0000 %Y'
                    epoch = int(mktime(strptime(date_time, pattern)))
                    if epoch_prev == 0:
                        epoch_prev = epoch

                    if epoch - epoch_prev == 60:
                        epoch_prev = epoch
                        hashtags_evolution.extend((epoch, len(hashtags_processed)))
                        if size_prev == 0:
                            new_tags = len(hashtags_processed)
                        else:
                            new_tags = len(hashtags_processed) - size_prev

                        size_prev = len(hashtags_processed)
                        with open('hashtags_evolution.txt', 'a') as f:
                            s = str(epoch) + ' ' + str(new_tags) + '\n'
                            f.write(s)
                        # print epoch, date_time

                    if 'entities' in data:
                        for hashtag in data['entities']['hashtags']:
                            # print hashtag['text']
                            if hashtag['text'] in hashtags_processed:
                                hashtags_processed[hashtag['text']]['count'] += 1
                                hashtags_processed[hashtag['text']]['user'].append(data['user']['screen_name'])
                            else:
                                hash_count += 1
                                hashtags_processed[hashtag['text']] = {}
                                hashtags_processed[hashtag['text']]['count'] = 1
                                hashtags_processed[hashtag['text']]['user'] = []
                                hashtags_processed[hashtag['text']]['user'].append(data['user']['screen_name'])
                except:
                    print(traceback.format_exc())
                    continue
        except KeyboardInterrupt:
            sys.exit()
        except:
            print(traceback.format_exc())

    print count, file_name
# print hashtags_evolution