""" VOWELS"""
def main():
    """
    main function   
    """
    str_input = input("Enter a string")
    vol_inp = 0
    con_inp = 0
    for i in str_input:
        if i in 'aeiou':
            vol_inp = vol_inp + 1
        else:
            con_inp = con_inp + 1
    print("Number of vol_inp")
    print(str(vol_inp))
if __name__ == "__main__":
    main()
