# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
    	smaller_value = b
    else:
    	smaller_value = a
    while smaller_value >= 1:
    	if a % smaller_value == 0 and b % smaller_value == 0:
    		break
    	smaller_value -=1
    return smaller_value
def main():
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]),int(data[1]))) 
if __name__ == "__main__":
    main()