from time import mktime, strptime
import json
import pprint
import os
import glob
import traceback

def to_UnixTime(inputDir = '../scripts/spam_users_timeline/', scriptsDir = '../../scripts'):    
    timeline_path = inputDir

    os.chdir(timeline_path)
    file_list = []
    for f in glob.glob("*.txt"):
        file_list.append(f)
    os.chdir(scriptsDir)    
    print len(file_list)

    i = 0
    for json_file in file_list:
        file_name = timeline_path + json_file
        i = i + 1
        with open(file_name, 'r') as f_in:
            with open(file_name + '_epoch', 'w') as f_out:

                line_num = 0
                for line in f_in:
                    try:
                        l = json.loads(line)                        
                    except:
                        print(traceback.format_exc())
                    	print "error", line, i
                    	continue
                    line_num += 1
                    if 'created_at' in l:
                	   date_time = l['created_at']
                    # print date_time
                    pattern = '%a %b %d %H:%M:%S +0000 %Y'
                    epoch = int(mktime(strptime(date_time, pattern)))
                    f_out.write(str(epoch) + '\n')
    	
    	print file_name, i, line_num
        if line_num != 1800:
            print "ERROR"
    print "complete"

if __name__ == "__main__":    
    to_UnixTime()