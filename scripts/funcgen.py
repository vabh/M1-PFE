f = open('todo.txt', 'r')

fg = open('met.java', 'w')

acess_specifier = 'public'
return_type = 'void'
for line in f:
	if '1' in line:
		comment = '//todo'
	else:
		comment = ''

	l = line.split(',')
	name = l[0].strip().replace(' ', '').replace('/','').replace(':', '')
	string = name + '()\n{\n\t'+ comment +'\n}\n'

	fg.write(acess_specifier + ' ' + return_type + ' ' +string)

	print string

f.close()
fg.close()
# s = acess_specifier + ' ' + return_type + 