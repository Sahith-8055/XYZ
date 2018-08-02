"""vowels"""

def main():
    """Vowel"""
    s_in = input()
    vol_inp = 0
    c_inp = 0
    for i in s_in:
        if i in 'aeiou':
            vol_inp = vol_inp + 1
        else:
            c_inp = c_inp + 1
    print(vol_inp)

if __name__ == "__main__":
    main()
