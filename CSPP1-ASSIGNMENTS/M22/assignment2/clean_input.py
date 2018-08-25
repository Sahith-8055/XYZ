'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
def clean_string(string):
    '''Clean string function'''
    string = ''.join([i for i in string if i.isalpha()])
    return string
def main():
    '''Main function'''
    string = input()
    print(clean_string(string))
if __name__ == '__main__':
    main()
