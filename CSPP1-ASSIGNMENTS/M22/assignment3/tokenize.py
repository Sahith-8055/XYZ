'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string):
    '''Tokenize function'''
    dictionary1 = {}
    new_string = string.split(' ')
    for word in new_string:
        if word not in dictionary1:
            dictionary1[word] = 1
        else:
            dictionary1[word] += 1
    return dictionary1
def main():
    '''Main function'''
    number_of_lines = int(input())
    string = ""
    for _ in range(number_of_lines):
        string += input()
    print(tokenize(string))
if __name__ == '__main__':
    main()
