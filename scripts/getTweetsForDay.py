import json
import pprint


# filename = "#HappyPiDaysearch-20150321-111140.txt"
# filename = "#HappyPiDaysearch-20150321-111624.txt"
# filename = "#HappyPiDaysearch-20150321-111818.txt"
# filename = "#HappyPiDaysearch-20150321-112112.txt"
# filename = "#HappyPiDaysearch-20150321-112218.txt"
# filename = "#HappyPiDaysearch-20150321-112343.txt"
# filename = "#HappyPiDaysearch-20150321-112421.txt"
# filename = "#HappyPiDaysearch-20150321-112859.txt"
filename = "#HappyPiDaysearch-20150321-113138.txt"

json_file = "tweets14.txt"

# out_file = 'tweets14.txt'
# f_out = open(out_file, 'a')
# data = json.loads(line)
with open(json_file, 'r') as f:
	for line in f:
		data = json.loads(line)
		created_at = data['created_at']
		print created_at
		# day = created_at.split()[2]
		# if day == '14':
		# 	f_out.write(line)

# f_out.close()

pprint.pprint(data)