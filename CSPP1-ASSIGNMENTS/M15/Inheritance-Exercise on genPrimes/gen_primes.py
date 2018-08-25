"""Generate n primes"""
def gen_primes():
    '''Function to write n primes'''
    number = 2
    prime = True
    while True:
        if prime is True:
            yield number
        number = number + 1
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        else:
            prime = True
def main():
    '''Writing inside this function'''
    n_input = int(input())
    primenum = gen_primes()
    for _ in range(n_input):
        print(primenum.__next__())
if __name__ == '__main__':
    main()
