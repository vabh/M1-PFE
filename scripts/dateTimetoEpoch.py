from time import mktime, strptime
import json
import pprint
import os
import glob

timeline_path = '../scripts/spam_users_timeline/'

os.chdir(timeline_path)
file_list = []
for f in glob.glob("*.txt"):
    file_list.append(f)
os.chdir('../../scripts')

print len(file_list)

i = 0
for json_file in file_list:
    file_name = timeline_path + json_file
    i = i + 1
    with open(file_name, 'r') as f_in:
        with open(file_name + '_epoch', 'w') as f_out:
            for line in f_in:
                try:
					l = json.loads(line)					
            	except:
                	print line
                	continue

            	date_time = l['created_at']
            	pattern = '%a %b %d %H:%M:%S +0000 %Y'
            	epoch = int(mktime(strptime(date_time, pattern)))
            	f_out.write(str(epoch) + '\n')
	
	print file_name, i