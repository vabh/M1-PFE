import os
import glob
import traceback
import json
from time import mktime, strptime
# os.chdir('../tweets/hillary')

# file_list = []
# for file in glob.glob("*.txt"):
# file_list.append(file)


# def bin_search(array, low, high, target):

#     while low <= high:

#         mid = (low + high) / 2
#         print array[mid]
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             print 'high - 1', array[mid]
#             high = mid - 1
#         elif array[mid] < target:
#             print 'low + 1', array[mid], target
#             low = mid + 1

#     return -1


# nums = [i for i in range(10, 20)]
# print nums
# print bin_search(array=nums, low=0, high=9, target=10)

file_name = '../scripts/spam_users_timeline/wildteens3.txt'
with open(file_name, 'r') as f_in:
    with open(file_name + '_epoch', 'w') as f_out:
        for line in f_in:
            try:
                l = json.loads(line)
                print l
            except:
                print(traceback.format_exc())
                print "error", line
                continue

            date_time = l['created_at']
            pattern = '%a %b %d %H:%M:%S +0000 %Y'
            epoch = int(mktime(strptime(date_time, pattern)))
            f_out.write(str(epoch) + '\n')
