import urllib,sys

def crawler(page):
    code = page.read()
    links = []
    while code.find('<a') is not -1:
        tag_begin = code.find('<a',0)
        code = code[tag_begin+2:]
        att_begin = code.find('href')
        code = code[att_begin+4:]
        link_begin = code.find('"')
        link_end = code.find('"',link_begin+1)
        if code[link_begin+1:link_end] not in links:
            links.append(code[link_begin+1:link_end])
        code = code[link_end:]
    return links

def link_counter(page):
    counter = 0
    code = page.read()
    while code.find('</a>') is not -1:
        counter = counter + 1
        code = code[code.find('</a>')+4:]
    return counter

# This function gets the input from command line
def main(argv):
    page = urllib.urlopen(argv[0])
    links = crawler(page)
    for link in links:
        print '"' + link + '"' + '\n'

if __name__ == "__main__":
	main(sys.argv[1:])
