def del_stop_word(str):
    str = str.lower().split()
    result = ''
    stop_words = ['a','an','and','are','as',
    'at','be','by','for','from',
    'has','he','in','is','it','its',
    'of','on','that','the','to','was',
    'were','will','with']

    for word in str:
        if word not in stop_words:
            result = result + ' ' + word
    return result

# This function gets the input from command line
def main(argv):
    if len(argv) == 0:
        print "For using dropper you should call it this way:\n" + "python3 del_stop_word.py -[QUERY]\n\tExample: word1 word2 word3"
    else:
        words = argv[2].split()
        words.sort()
        docPath = argv[1]
        if argv[0] == "-pdf":
            index = pdfIndexer(words,docPath)
        elif argv[0] == "-web":
            index = webPageIndexer(words,docPath)
        for key in index.keys():
            print key , '=>' , index[key] , '\n'

if __name__ == "__main__":
	main(sys.argv[1:])
