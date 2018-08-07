"""Exercise: fourth power"""
def square(x_inp):
    """square"""
    return x_inp**2
def fourth_power(x_inp):
    '''
    x: int or float.
    '''
    return x_inp**4
def main():
    """Writing inside this main function"""
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourth_power(int(float(str(data)))))
    else:
        print(fourth_power(data))
if __name__ == "__main__":
    main()
