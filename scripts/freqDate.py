filename = '../tweets/freq.txt';

reqday = 14

fout = open('../tweets/out.txt', 'w')

with open(filename, 'r') as f:
	for line in f:
		line = line.split()
		day = line[3]
		if day == '14': 
			id = line[0]
			time = line[4].split(':')
			
			h = time[0]
			m = time[1]
			s = time[2]
			# t = (int(h) * 60 + int(m)) * 60 + int(s)
			t = h + ',' + m + ',' + s
			fout.write(str(line[4]) + '\n')
fout.close()