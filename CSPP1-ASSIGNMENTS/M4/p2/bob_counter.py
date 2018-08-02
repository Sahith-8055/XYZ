""""Finding the bob"""
def main():
    """defining main Subset """
    var_a = input()
    var_b = 'bob'
    count = 0
    for i in range(len(var_a)):
        if var_b == var_a[i:i+3]:
            count = count + 1
    print(str(count))
if __name__ == "__main__":
    main()
