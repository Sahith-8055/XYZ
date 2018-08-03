"""Guess a number"""
LOW_INP = 0
HIGH_INP = 100
MIDDLE_INP = (LOW_INP + HIGH_INP)/2
GUESS_I = 'h'
while GUESS_I != 'c':
    print("Is your secret number", MIDDLE_INP, "?")
    print("Enter 'h' to indicate guess is too high.")
    print("Enter 'l' to indicate the guess is too low.")
    print("Enter 'c' to indicate I guessed correctly.")
    GUESS_I = input()
    if GUESS_I == 'h':
        HIGH_INP = MIDDLE_INP
        MIDDLE_INP = int((LOW_INP + HIGH_INP)/2)
    if GUESS_I == 'l':
        LOW_INP = MIDDLE_INP
        MIDDLE_INP = int((LOW_INP + HIGH_INP)/2)
    if GUESS_I != 'c':
        print("Sorry, I didn't understand your input")
print("Game Over")
print("Your secret number is ", MIDDLE_INP)
