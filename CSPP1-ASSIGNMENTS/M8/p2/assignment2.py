"""Exercise: Assignment-2.This function takes in one number and returns one number."""
def sumofdigits(n_inp):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if n_inp == 0:
        return 0
    return (n_inp%10) + sumofdigits(n_inp//10)
def main():
    '''Writing inside this function'''
    a_in = input()
    print(sumofdigits(int(a_in)))
if __name__ == "__main__":
    main()
