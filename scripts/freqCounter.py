import operator

filename = '../tweets/out.txt';

reqday = 14

time = {}
with open(filename, 'r') as f:
	for line in f:
		index = line.strip()
		index = index.split(':')
		index = index[0] + ':' + index[1]
		if index in time:
			time[index] = time[index] + 1;
		else:
			time[index] = 1

mtime =  max(time, key = time.get)

sorted_x = sorted(time.items(), key=operator.itemgetter(1), reverse=True)



with open('freqSec.txt', 'w') as f:
	for i in sorted_x:
		f.write(str(i[0]) + ', ' + str(i[1]) + '\n')
