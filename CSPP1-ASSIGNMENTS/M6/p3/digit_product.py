'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    add = 1
    i = 1
    while i <= int_input:
        rem = int_input%10
        add = add*rem
        int_input = int_input//10
    print(add)
if __name__ == "__main__":
    main()
