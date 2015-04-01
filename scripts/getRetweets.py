import json

tweet_id = 576606932686872576

filename = '#HappyPiDaysearch-20150321-113138.txt'
in_file = '../tweets/' + filename

outfile = 'tweetodgod.txt'
f_out = open(outfile, 'a')
with open(in_file, 'r') as f:
	for line in f:
		data = json.loads(line)
		if 'retweet_count' in data and 'retweeted_status' in data:
			if data['retweeted_status']['id'] == tweet_id:			
				t_id = data['id']
				date = data['created_at'].split()[3]
				day = data['created_at'].split()[2]
				if day == '14':
					f_out.write(str(t_id) + ', ' + date +'\n')
							
f_out.close()