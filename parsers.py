def parse_fasta(text):
	#takes a string
	#returns a dictionary
	result = {}
	text = text.split('>')
	for item in text:
		item = item.replace(r'"\n"', '')
	print (text)



if __name__ == "__main__":
	f = open ('example.fa', 'r')
	text = f.read()
	f.close()
	parse_fasta(text)
