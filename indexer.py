import urllib,sys,PyPDF2

def pdfIndexer(words,docPath):
    document = open(docPath,'rb')
    pages = getPages(document)
    index = {}
    for word in words:
        index[word] = None
    for word in words:
        postings = []
        for page in pages:
            if page.find(word) != -1:
                postings.append(pages.index(page)+1)
        index[word] = (document.name,postings)
    return index

def webPageIndexer(words,url):
    page = urllib.urlopen(url).read()
    index = []
    for word in words:
        if page.find(word) != -1:
            index.append(word)
    return {url:index}

def getPages(docFile):
    pdf = PyPDF2.PdfFileReader(docFile)
    pages = []
    for i in range(pdf.numPages):
        page = pdf.getPage(i)
        pages.append(page.extractText())
    return pages

# This function gets the input from command line
def main(argv):
    if len(argv) == 0:
        print "For using indexer you should call it this way:\n" + "python indexer.py -[OPTION] [PATH] [WORDS]\n" + "[OPTION]: \n\t-pdf for indexing pdf files \n\t-web for indexing web pages\n" + "[WORDS]: Separated by spaces:\n\t word1 word2 word3"
    else:
        words = argv[2].split()
        docPath = argv[1]
        if argv[0] == "-pdf":
            index = pdfIndexer(words,docPath)
        elif argv[0] == "-web":
            index = webPageIndexer(words,docPath)
        for key in index.keys():
            print key , '=>' , index[key] , '\n'

if __name__ == "__main__":
	main(sys.argv[1:])
