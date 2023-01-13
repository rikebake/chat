#chat 格式更新3


# read the file
chat_list = []
with open('3.txt','r',encoding = 'utf-8-sig') as file:
	for line in file:
		chat_list.append(line.strip())

for line in chat_list:
	s = line.split(' ')
	time = s[0][:5] # to take out element of index 0 / 1/ 2 /3 /4
	name = s[0][5:] # to take out element of index 5 to the end 
	print(s)
	print(time)
	print(name)