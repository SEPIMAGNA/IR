import sys
# This method stem a given word using porter algorithm
def stem(str):
	""" First we normalize our word """
	word = normalize(str)
	""" Then we define our rules """
	rules = (('sses','ss'),('ies','i'),('ss',''),('s',''),('eed','ee'),('ed',''),('ing',''))
	""" Now we check if we can apply a rule to the word """
	for rule in rules:
		if len(word) > len(rule[0]):
			if word.find(rule[0]) + len(rule[0]) == len(word):
				if len(word[:word.find(rule[0])])>1:
					return 'Stemmed form of ' + str + ' is ' + word[:word.find(rule[0])] + rule[1]
				else:
					return 'Stemmed form of ' + str + ' is ' + word
# This method applies a simple normalization on word
def normalize(str):
	word = str.strip()
	word = word.lower()
	return word
# This function gets the input from command line
def main(argv):
	stemmed_word = stem(argv[0])
	if stemmed_word == None:
		print "No such stem"
	else:
		print stemmed_word

if __name__ == "__main__":
	main(sys.argv[1:])
