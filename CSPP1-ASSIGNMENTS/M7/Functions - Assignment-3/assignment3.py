"""Functions - Assignment-3 - Using Bisection Search to Make the Program Faster."""
def paying_debt(balance, annual_interest_rate):
    """ Calculating the interest"""
    monthly_interest_rate = (annual_interest_rate) / 12.0
    monthly_payment_lower_value = balance / 12.0
    monthly_payment_upper_value = (balance * (1 + monthly_interest_rate)**12) / 12.0
    new_balance = balance
    eps = 0.0001
    guess_inp = (monthly_payment_lower_value + monthly_payment_upper_value)/2.0
    while True:
        month = 1
        while month <= 12:
            new_balance = new_balance - guess_inp
            new_balance = new_balance + (monthly_interest_rate * new_balance)
            month += 1
        if new_balance > 0 and new_balance > eps:
            monthly_payment_lower_value = guess_inp
            new_balance = balance
        elif new_balance < 0 and new_balance < -eps:
            monthly_payment_upper_value = guess_inp
            new_balance = balance
        else:
            return guess_inp

        guess_inp = (monthly_payment_lower_value + monthly_payment_upper_value)/2
def main():
    """Writing inside this function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", paying_debt(data[0], data[1]))
if __name__ == "__main__":
    main()
