"""Exercise : Biggest Exercise."""
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    i_inp = 0
    L = []
    if len(aDict) == 0:
    	return 0
    print(aDict)
    for k in aDict:
    	if len(aDict[k]) >= i_inp:
    		i_inp = len(aDict[k])
    		L = k
    return str(L)
def main():
	n=input()
	aDict={}
	for i in range(int(n)):
		s=input()
		l=s.split()
		if l[0] not in aDict:
			aDict[l[0]]=[l[1]]
		else:
			aDict[l[0]].append(l[1])
	print(biggest(aDict))
if __name__ == "__main__":
	main()