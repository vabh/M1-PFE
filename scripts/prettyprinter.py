import json
import pprint

filename = "../tweets/#HillaryClintonsearch-20150414-093533.txt"
json_file = open("" + filename)

line = json_file.readline()
line = json_file.readline()
data = json.loads(line)

var = 'user_mentions'

u = data['user_mentions']
print u[0]['screen_name']
# pprint.pprint(u)
