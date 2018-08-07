"""This function takes in two arguments character and String and returns one boolean value."""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    
def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))
if __name__ == "__main__":
    main()