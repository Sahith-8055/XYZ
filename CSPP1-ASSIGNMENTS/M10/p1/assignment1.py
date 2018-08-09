'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter
a list of letters, letters_guessed.
'''
def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letter_count = dict((key, 0) for key in string.ascii_lowercase)
    str_out = ''
    for char in letter_count.keys():
        if char not in letters_guessed:
            str_out = str_out + char
    return str_out
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))
if __name__ == "__main__":
    main()
