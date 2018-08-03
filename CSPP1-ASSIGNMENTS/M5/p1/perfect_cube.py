"""Write a python program to find if the given number is a perfect cube or not"""
def main():
    """Writing inside the main function"""
    num_input = int(input())
    cube_root = 0
    while cube_root**3 < abs(num_input):
        cube_root = cube_root + 1
    if cube_root**3 != abs(num_input):
        print(str(num_input) + " is not a perfect cube")
    else:
        print("Cube root of " +  str(num_input) +  "is"  +  str(cube_root))
if __name__ == "__main__":
    main()
