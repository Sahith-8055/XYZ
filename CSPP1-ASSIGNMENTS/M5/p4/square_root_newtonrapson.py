"""Write a python program to find the square root of the given number using newton raphson method"""
def main():
    """Writing inside the function"""
    squar_root = int(input())
    epsilon = 0.01
    guess = squar_root/2.0
    num_guesses = 0
    while abs(guess**2 - squar_root) >= epsilon:
        num_guesses += 1
        guess = guess - (((guess**2) - squar_root)/(2*guess))
    print(str(guess))
if __name__ == "__main__":
    main()
