"""Exercise: odd.This function takes in one number and returns a boolean."""
def odd(x_inp):
    '''
    x: int or float.
    returns: True if x is odd, False otherwise '''
    return x_inp%2 != 0
def main():
    """Writing inside this function"""
    data = input()
    print(odd(int(data)))
if __name__ == "__main__":
    main()
