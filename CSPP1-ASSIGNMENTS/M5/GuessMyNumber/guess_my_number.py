"""Guess My Number Exercise"""
def main():
    """Writing the function"""
    low_inp = 0
    high_inp = 100
    middle_inp = (low_inp + high_inp)/2
    guess_i = 'h'
    while guess_i != 'c':
        print("Is your secret number", middle_inp, "?")
        print("Enter 'h' to indicate guess is too high.")
        print("Enter 'l' to indicate the guess is too low.")
        print("Enter 'c' to indicate I guessed correctly.")
        guess_i = input()
        if guess_i == 'h':
            high_inp = middle_inp
            middle_inp = int((low_inp + high_inp)/2)
        if guess_i == 'l':
            low_inp = middle_inp
            middle_inp = int((low_inp + high_inp)/2)
        if guess_i != 'c':
            print("Sorry, I didn't understand your input")
    print("Game Over")
    print("Your secret number is ", middle_inp)
if __name__ == "__main__":
    main()
