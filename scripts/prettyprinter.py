import json
import pprint

filename = "#HappyPiDaysearch-20150321-112421.txt"
json_file = open("../tweets/" + filename)

line = json_file.readline()
# line = json_file.readline()
data = json.loads(line)

var = 'created_at'
id_s = str(data[var])

# print id_s
pprint.pprint(data)