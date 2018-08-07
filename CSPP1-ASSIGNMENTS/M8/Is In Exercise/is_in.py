"""This function takes in two arguments character and String and returns one boolean value."""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    length_str = len(aStr)
    middle_char = length_str // 2
    if length_str == 0:
        return False
    if length_str == 1:
        if char == aStr:
            return True
        else:
            return False
    if aStr[middle_char] == char:
        return True
    elif aStr[middle_char] > char:
        return isIn(char,aStr[0:middle_char])
    else:
        return isIn(char,aStr[middle_char:length_str+1])
def main():
    ''' Writing inside this function'''
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))
if __name__ == "__main__":
    main()
