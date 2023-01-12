#<<<Chat format change 2rd>>>

#<<<read file>>> 
def read_file(filename):
	chat_list = []
	with open(filename, 'r',encoding = 'utf-8-sig') as file:
		for line in file:
			chat_list.append(line.strip())
	return chat_list 

#<<< convert the format>>>
def convert(chat_list): # in order to calculate how many words that Allen and Vick texted 
	chat_convert = []
	person = None # to prevent crash by "person" in row 23
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0 
	viki_image_count = 0 

	for line in chat_list:
		line_list = line.split(' ') # when get a "space", split it, we wanna get the conversation only
		time = line_list[0]
		name = line_list[1] 
		if name == 'Allen':
			if line_list[2] == '貼圖':
				allen_sticker_count += 1
			elif  line_list[2] == '圖片':
				allen_image_count += 1
			else:
				for m in line_list[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if line_list[2] == '貼圖':
				viki_sticker_count += 1
			elif  line_list[2] == '圖片':
				viki_image_count += 1
			else:
				for m in line_list[2:]:
					viki_word_count+=len(m)
	print('allen text ', allen_word_count,'allen sticker count', allen_sticker_count, 'allen image ', allen_image_count ) # count the text that allen sent
	print('Viki text ', viki_word_count, 'viki sticker count', viki_sticker_count,'viki image ', viki_image_count)


#<<< write the flle >>>
def write_file(filename, chat_convert):
	with open(filename,'w',encoding = 'utf-8-sig') as file:
		for line in chat_convert:
			file.write(line + '\n')

def main():
	chat = read_file('LINE-Viki.txt')
	print(chat)
	chat_convert = convert(chat)
	print('============')
	print(chat_convert)
	#write_file('out.txt',chat_convert )

main()