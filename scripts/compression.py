import json
import pprint
import os
import glob
import bz2
from shutil import copyfileobj
import traceback

tweets_path = '../tweets/piday/'
# tweets_path = ''

os.chdir(tweets_path)
file_list = []
for f in glob.glob("*.bz2"):
    file_list.append(f)
os.chdir('../../scripts')

print file_list
compress = 2
if compress == 1:
    for json_file in file_list:
        file_name = tweets_path + json_file
        with open(file_name, 'rb') as input:
            with bz2.BZ2File(file_name + '.bz2', 'wb', compresslevel=9) as output:
                copyfileobj(input, output)
        print file_name

# decompression

else:
	count = 0
	for json_file in file_list:

		file_name = tweets_path + json_file

		with bz2.BZ2File(file_name, 'rb') as f:
			with open(file_name + '.txt', 'w') as f_out:
				try:
					for line in f:
						try:
							# data = json.loads(json.dumps(eval(line)))
							# data = json.loads(line)

							count += 1	
							# for hashtag in data['entities']['hashtags']:
							# 	print hashtag['text']
							# print json.dumps(eval(line))
							# json.dumps(eval(line), f_out)
							# f_out.write(str(data))
							# f_out.write('\n')
						except:
							print(traceback.format_exc())
							continue
				except:
					print(traceback.format_exc())

		print file_name

print count
