'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.
    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for i in sudoku:
        for j in i:
            if j not in '1234567890':
                return False
    return True
def count(sudoku):
    transpose = zip(*sudoku)
    for i in sudoku:
        for j in i:
            if i.count(j) != 1 and i.count(j) >= 1:
                return False
    for k in transpose:
        for l in k:
            if k.count(l) != 1 and k.count(l) >= 1:
                return False        
    return True
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []
    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
        sudoku1 = sudoku
        input_1 = check_sudoku(sudoku)
    # call solution function and print result to console
    if input is True:
        print(count(sudoku1))
    input_2 = count(sudoku1)    
if __name__ == '__main__':
    main()
