import json
import pprint

filename = "#HappyPiDaysearch-20150321-112421.txt"
json_file = open("../tweets/" + filename)

freq_file = open("../tweets/peak1.txt", 'a')

time_start_hour = "13"
time_start_min = "10"

time_end_hour = "13"
time_end_min = "59"

for line in json_file:
	data = json.loads(line)
	id_s = str(data['id'])
	date = data['created_at'].split()
	
	day = date[2]
	
	time =  date[3].split(':')
	h = time[0]
	m = time[1]
	s = time[2]
	
	# print date[2]
	
		
	if day == "14" and h == time_start_hour:
		
		if m >= time_start_min and m <= time_end_min:

			date = data['created_at'].encode('utf-8').strip()
			text = data['text'].encode('utf-8').strip()
		
			freq_file.write(id_s + ", " + date + ", " + text +"\n")

freq_file.close()
json_file.close()
# pprint.pprint(data)