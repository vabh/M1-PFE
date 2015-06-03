import json
import pprint
import os
import glob
import bz2
from shutil import copyfileobj
import traceback

tweets_path = '../tweets/'
# tweets_path = ''

os.chdir(tweets_path)
file_list = []
for f in glob.glob("*stream*.bz2"):
    file_list.append(f)
os.chdir('../scripts')

# print file_list
compress = 2

if compress == 1:
    for json_file in file_list:
        file_name = tweets_path + json_file
        with open(file_name, 'rb') as input:
            with bz2.BZ2File(file_name + '.bz2', 'wb', compresslevel=9) as output:
                copyfileobj(input, output)
        print file_name
else:
    for json_file in file_list:
        file_name = tweets_path + json_file
    	with bz2.BZ2File(file_name, 'rb') as f:
    		with open(file_name + '.txt', 'w') as f_out:
    			try:
        			for line in f:
        				f_out.write(line)
        		except:
        			print(traceback.format_exc())

        print file_name
