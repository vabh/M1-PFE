# import json
# import pprint

# filename = "tweet_ids_16clinton_hashtags.txt"
# json_file = open("" + filename)

# line = json_file.readline()
# line = json_file.readline()
# data = json.loads(line)

# var = 'created_at'
# # id_s = str(data[])
# for e in data['hashtags']:
# 	print e
# # print id_s
# # pprint.pprint(data)

l = {}
for i in range(1, 10):
	
	a = i % 2

	if str(a) in l:
		# print i
		l[str(a)].append(i)
	else:
		l[str(a)] = []
# print l
# print len(l['0'])

for i in range(0, 4):
		print i