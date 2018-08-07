""" Write a Python function, factorial(n)"""
def factorial(n_inp):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if n_inp in (0, 1):
        return 1
    return n_inp * factorial(n_inp-1)
def main():
    """Writing inside this function"""
    a_inp = input()
    print(factorial(int(a_inp)))
if __name__ == "__main__":
    main()
