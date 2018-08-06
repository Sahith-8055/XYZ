"""Assignment-2 - Paying Debt off in a Year."""
def paying_debtoff(balance1, annual_interest_rate):
    """Calculating the interest"""
    fixedpayment = 0
    balance = balance1
    while balance > 0:
        balance = balance1
        month = 1
        monthly_interest_rate = annual_interest_rate / 12.0
        fixedpayment += 10
        while month <= 12:
            monthly_unpaid_balance = balance - fixedpayment
            updated_balance = monthly_unpaid_balance+(monthly_interest_rate*monthly_unpaid_balance)
            balance = updated_balance
            month += 1
    return fixedpayment
def main():
    """Writing inside this function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", paying_debtoff(data[0], data[1]))
if __name__ == "__main__":
    main()
