import os
import glob

os.chdir('../tweets/hillary')

file_list = []
for file in glob.glob("*.txt"):
    file_list.append(file)

print file_list