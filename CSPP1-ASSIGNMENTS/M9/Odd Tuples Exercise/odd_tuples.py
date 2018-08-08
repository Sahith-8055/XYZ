"""Exercise : Odd Tuples"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup. 
    '''
    odd_tuple = ()
    k = 0
    for i in aTup:
    	if k % 2 ==0:
    		odd_tuple = odd_tuple + (i, )
    	k +=1	
    return odd_tuple
def main():
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += (str(data[j]),)
    print(oddTuples(aTup))
if __name__ == "__main__":
    main()
