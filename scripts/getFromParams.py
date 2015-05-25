import json
import operator
import pprint

file_name = 'iphone_data.txt'

hash_list = {}
with open(file_name, 'r') as f:
	for line in f:
		data = json.loads(line)
		if data.get('hashtags'):
			user = data['user']
			id = data['id']			
			
			hashtags_data = str(data.get('hashtags'))

			if hashtags_data in hash_list:
				hash_list[hashtags_data]['count'] = hash_list[hashtags_data]['count'] + 1
				hash_list[hashtags_data]['id'].append(id)
				hash_list[hashtags_data]['user'].append(user)
			else:
				hash_list[hashtags_data] = {}
				hash_list[hashtags_data]['count'] = 1
				hash_list[hashtags_data]['id'] = []
				hash_list[hashtags_data]['id'].append(id)
				hash_list[hashtags_data]['user'] = []
				hash_list[hashtags_data]['user'].append(user)

sorted_x = sorted(hash_list.items(), key=operator.itemgetter(1), reverse=True)

with open('co-hashtags.txt', 'w') as f:
	for i in range(0, 100):
		f.write(sorted_x[i][0] + ', ' + str(sorted_x[i][1]['count']))
		f.write('\n')


with open('iphone-spam-user-list.txt', 'w') as f:
	for user in sorted_x[0][1]['user']:
		f.write(user)
		f.write('\n')