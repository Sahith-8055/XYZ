'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    '''Main function'''
    number_of_lines = int(input())
    string = ""
    for _ in range(number_of_lines):
        string += input() + "\n"
    print(string)
if __name__ == '__main__':
    main()
