import json
import pprint
import os
import glob

tweets_path = '../tweets/hillary/'

os.chdir(tweets_path)
file_list = []
for f in glob.glob("*.txt"):
    file_list.append(f)
os.chdir('../../scripts')


out_file_name = 'test.txt'

with open(out_file_name, 'w') as f_out:
	for json_file in file_list:	

		file_name = tweets_path + json_file
		print file_name
		with open(file_name, 'r') as f:
			for line in f:
				l = json.loads(line)
				data = {}
				data['time'] = l['created_at'].split()[3]
				data['day'] = l['created_at'].split()[2]
				data['id'] = l['id']		
				data['user'] = l['user']['screen_name']

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
			# print data

# pprint.pprint(data)