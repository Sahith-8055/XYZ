'''Exercise : Assignment-2'''
import random
WORDLIST_FILENAME = "words.txt"
def loadWords():
    """Returns a list of valid words. Words are strings of lowercase letters."""
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def chooseWord(wordlist):
    """wordlist (list): list of words (strings)"""
    return random.choice(wordlist)
wordlist = loadWords()
import random
def loadWords():
    WORDLIST_FILENAME = "words.txt"
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count_word = 0
    for char_1 in secret_word:
        if char_1 in letters_guessed:
            count_word += 1
    if count_word == len(secret_word):
        return True
    return False
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.'''
    string_new = ''
    for char_1 in secretWord:
        if char_1 in lettersGuessed:
            string_new += char_1
        else:
            string_new += '_'
    return string_new 
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letter_count = dict((key, 0) for key in string.ascii_lowercase)
    string_new = ''
    for char in letter_count.keys():
        if char not in lettersGuessed:
            string_new = string_new + char
    return string_new
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 8
    wordGuessed = False
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is ' + str(intro) + ' letters long.')
    print ('------------')
    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ('You have ' + str(mistakesMade) + ' guesses left.')
        print ('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print ('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
    if wordGuessed == True:
        print('Congratulations, you won!')
    elif mistakesMade == 0:
        print ('Sorry, you ran out of guesses. The word was ' + str(secretWord))
def main():
    '''
    Main function for the given program   
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
if __name__ == "__main__":
    main()
