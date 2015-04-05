import json
import pprint

filename = "tweets14.txt"
# filenameaux = 'tweetsaux.txt'
with open(filename, 'r') as f:
	for line in f:
		data = json.loads(line)
		t = data['created_at']

		with open(filename, 'r') as f2:
			for line2 in f2:
				data2 = json.loads(line)
				t2 = data['created_at']
				print t2


# pprint.pprint(data)