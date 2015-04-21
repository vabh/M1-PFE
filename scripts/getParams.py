import json
import pprint

# json_file = "##Hillary2016search-20150415-094350.txt"
# json_file = "##Hillary2016search-20150415-094556.txt"
# json_file = "##Hillary2016search-20150415-094858.txt"
# json_file = "##Hillary2016search-20150415-095020.txt"
# json_file = "##Hillary2016search-20150415-095123.txt"
# json_file = "##Hillary2016search-20150415-095433.txt"
# json_file = "##Hillary2016search-20150415-100313.txt"
# json_file = "##Hillary2016search-20150415-100407.txt"
# json_file = "##Hillary2016search-20150415-100952.txt"
# json_file = "##Hillary2016search-20150415-101754.txt"

# json_file = "#Hillary2016search-20150415-102332.txt"
# json_file = "#Hillary2016search-20150415-102745.txt"
# json_file = "#Hillary2016search-20150415-102958.txt"

# json_file = '#Hillary2016search-20150418-121335.txt'
# json_file = '#Hillary2016search-20150418-122637.txt'
# json_file = '#Hillary2016search-20150418-123814.txt'
json_file = '#Hillary2016search-20150418-151250.txt'

json_file = "../tweets/" + json_file
out_file = 'tweet_ids_16clinton_hashtags.txt'
f_out = open(out_file, 'a')

with open(json_file, 'r') as f:
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
f_out.close()

# pprint.pprint(data)