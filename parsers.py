import global_variables

def parse_fasta(text,):
	#takes a string
	#returns a dictionary

	result = {}

	text = text.split('>')

	for item in text:

		if len(item)>0:

			result[item.split('\n')[0]] = ''.join(item.split('\n')[1::])
			global_variables.sequences[item.split('\n')[0]] = ''.join(item.split('\n')[1::])

	return result



if __name__ == "__main__":
	f = open ('example.fa', 'r')
	text = f.read()
	f.close()
	parse_fasta(text)
