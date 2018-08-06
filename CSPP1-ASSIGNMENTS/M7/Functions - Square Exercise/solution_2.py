"""Exercise: square. This function takes in one number and returns one number."""
def square(x_in):
    '''
    x: int or float.
    '''
    return x_in**2
def main():
    """Writing inside the main function"""
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))

if __name__ == "__main__":
    main()
