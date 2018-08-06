"""Functions | Assignment-1 - Paying Debt off in a Year"""
def paying_debt(balance, annual_interest_rate, monthly_paymentrate):
    """Finding the interest"""
    monthly_interestrate = annual_interest_rate / 12.0
    updated_balance = balance
    month_inp = 1
    while month_inp <= 12:
        minimum_monthly_payment = monthly_paymentrate * updated_balance
        monthly_unpaid_balance = updated_balance - minimum_monthly_payment
        updated_balance = monthly_unpaid_balance + (monthly_unpaid_balance * monthly_interestrate)
        month_inp += 1
    print("Remaining balance:", round(updated_balance, 2))
def main():
    """Writing inside this function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    paying_debt(data[0], data[1], data[2])
if __name__ == "__main__":
    main()
