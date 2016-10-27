import sys
def edit_distance(str,str2):
    m = []
    temp = []
    for i in range(len(str)):
        for j in range(len(str2)):
            temp.append(0)
        m.append(temp)
        temp = []
    for i in range(len(str)):
        m[i][0] = i
    for j in range(len(str2)):
        m[0][j] = j
    for i in range(len(str)):
        for j in range(len(str2)):
            if str[i] == str2[j]:
                m[i][j] = min(m[i-1][j-1],m[i-1][j] + 1,m[i][j-1] + 1)
            else:
                m[i][j] = min(m[i-1][j-1]+1,m[i-1][j] + 1,m[i][j-1] + 1)
    return m[len(str)-1][len(str2)-1]

# This function gets the input from command line
def main(argv):
    if argv[0] == '' and argv[1] == '':
        print 'Please insert both of the strings:\n'
    else:
        print 'The edit distance between ' + str(argv[0]) + ' and ' + str(argv[1]) + ' is ' + str(edit_distance(argv[0],argv[1]))

if __name__ == "__main__":
	main(sys.argv[1:])
