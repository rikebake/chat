#<<<Chat format change>>>

#<<<read file>>> 
def read_file(filename):
	chat_list = []
	with open(filename, 'r',encoding = 'utf-8-sig') as file:
		for line in file:
			chat_list.append(line.strip())
	return chat_list 

#<<< convert the format>>>
def convert(chat_list):
	chat_convert = []
	person = None # to prevent crash by "person" in row 23
	for line in chat_list:
		if line == 'Allen': 
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # if person has value, do the following. if none, do nothing
			chat_convert.append(person + ': ' + line)
	return chat_convert

#<<< write the flle >>>
def write_file(filename, chat_convert):
	with open(filename,'w',encoding = 'utf-8-sig') as file:
		for line in chat_convert:
			file.write(line + '\n')

def main():
	chat = read_file('input.txt')
	print(chat)
	chat_convert = convert(chat)
	print('============')
	print(chat_convert)
	write_file('out.txt',chat_convert )

main()