import json
import pprint

filename = "#HillaryClintonsearch-20150414-094917.txt"
filename = "#HillaryClintonsearch-20150414-095437.txt"
filename = "#HillaryClintonsearch-20150414-101119.txt"

# json_file = "tweetsClinton.txt"

out_file = 'tweets14.txt'
f_out = open(out_file, 'a')
data = json.loads(line)
with open(filename, 'r') as f:
	for line in f:
		data = json.loads(line)
		created_at = data['created_at']
		print created_at
		day = created_at.split()[2]
		if day == '12':
			f_out.write(line)

f_out.close()

# pprint.pprint(data)