"""Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in
which the letters occur in alphabetical order."""
def main():
    """To print the longest alphabetical series"""
    a_var = input()
    c_max = 0
    d_gain = 0
    count_1 = 0
    for i in range(len(a_var)-1):
        if a_var[i] <= a_var[i+1]:
            count_1 += 1
        else:
            count_1 = 0
        if d_gain < count_1:
            d_gain = count_1
            c_max = i
    d_max = c_max - d_gain + 1
    print(a_var[d_max:d_max+d_gain+1])
if __name__ == "__main__":
    main()
