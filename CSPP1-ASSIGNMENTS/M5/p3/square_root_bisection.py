"""Write a python program to find the square root of the given number"""
def main():
    """Writing in this function"""
    squar_root = int(input())
    epsilon_1 = 0.01
    lower_bound = 0.0
    upper_bound = squar_root
    ans = (upper_bound + lower_bound)/2.0
    while abs(ans**2 - squar_root) >= epsilon_1:
        if ans**2 < squar_root:
            lower_bound = ans
        else:
            upper_bound = ans
        ans = (upper_bound + lower_bound)/2.0
    print(str(ans) + ' is close to square root of ' + str(squar_root))
if __name__ == "__main__":
    main()
