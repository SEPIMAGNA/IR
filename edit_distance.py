import sys
def edit_distance(str,str2):
    #check to see if strings are empty
    if len(str) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str)

    distance = [[0 for i in range(len(str2)+1)] for j in range(len(str)+1)]
    for i in range(1,len(str)+1):
        distance[i][0] = i
    for j in range(1,len(str2)+1):
        distance[0][j] = j
    for i in range(1,len(str)+1):
        for j in range(1,len(str2)+1):
            if str[i-1] == str2[j-1]:
                distance[i][j] = min(distance[i-1][j-1],distance[i-1][j] + 1,distance[i][j-1] + 1)
            else:
                distance[i][j] = min(distance[i-1][j-1]+1,distance[i-1][j] + 1,distance[i][j-1] + 1)
    for i in range(len(distance)):
        print distance[i] , '\n'
    return distance[len(str)][len(str2)]

# This function gets the input from command line
def main(argv):
    if argv[0] == '' and argv[1] == '':
        print 'Please insert both of the strings:\n'
    else:
        print 'The edit distance between ' + str(argv[0]) + ' and ' + str(argv[1]) + ' is ' + str(edit_distance(argv[0],argv[1]))

if __name__ == "__main__":
	main(sys.argv[1:])
