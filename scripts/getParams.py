import json
import pprint

json_file = "tweets14.txt"

out_file = 'tweet_ids.txt'
f_out = open(out_file, 'a')

with open(json_file, 'r') as f:
	for line in f:
		l = json.loads(line)
		data = {}
		data['time'] = l['created_at'].split()[3]
		data['id'] = l['id']		
		data['retweeted'] = l['retweeted']
		if 'retweeted_status' in l:
			data['retweeted_status_id'] = l['retweeted_status']['id']
			data['retweet_count'] = l['retweet_count']
		else:
			data['retweeted_status_id'] = -1
			data['retweet_count'] = 0
		
		print data
f_out.close()

# pprint.pprint(data)