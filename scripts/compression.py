import json
import pprint
import os
import glob
import bz2
from shutil import copyfileobj

tweets_path = '../tweets/video/'
# tweets_path = ''

os.chdir(tweets_path)
file_list = []
for f in glob.glob("*.txt"):
    file_list.append(f)
os.chdir('../../scripts')


for json_file in file_list:
    file_name = tweets_path + json_file
    with open(file_name, 'rb') as input:
        with bz2.BZ2File(file_name + '.bz2', 'wb', compresslevel=9) as output:
        	copyfileobj(input, output)
    print file_name
