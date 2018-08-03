"""Write a python program to find the square root of the given number"""
def main():
    """Writing inside this function"""
    squ_apprx = int(input())
    epsilon_1 = 0.01
    guess_1 = 0.0
    step = 0.1
    num_guesses = 0
    while abs(guess_1**2 - squ_apprx) >= epsilon_1 and guess_1 <= squ_apprx:
        guess_1 += step
        num_guesses += 1
    print('num_guesses =', num_guesses)
    if abs(guess_1**2 - squ_apprx) >= epsilon_1:
        print('Failed on square root of', squ_apprx)
    else:
        print(guess_1)
if __name__ == "__main__":
    main()
