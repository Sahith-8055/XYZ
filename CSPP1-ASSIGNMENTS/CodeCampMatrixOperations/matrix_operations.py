def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    m1_rows = len(m1)
    m1_columns = len(m1[0])
    m2_rows = len(m2)
    m2_columns = len(m2[0])
    result_matrix = []
    result_matrix = [0] * m1_rows
    for r in range(m1_rows):
        result_matrix[r] = [0] * m1_columns
    if m1_columns == m2_rows:
        for r in range(m1_rows):
            for c in range(m2_columns):
                for t in range(m2_rows):
                    result_matrix[r][c] += int(m1[r][t]) * int(m2[t][c])
        return result_matrix
    else:
        print("Error: Matrix shapes invalid for mult")
        return None                
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    m1_rows = len(m1)
    m1_columns = len(m1[0])
    m2_rows = len(m2)
    m2_columns = len(m2[0])
    result_matrix = []
    result_matrix = [0] * m1_rows
    for r in range(m1_rows):
        result_matrix[r] = [0] * m1_columns
    if m1_rows == m2_rows and m1_columns == m2_columns:
        for r in range(m1_rows):
            for c in range(m1_columns):
                result_matrix[r][c] = int(m1[r][c]) + int(m2[r][c])
        return result_matrix
    else:
        print("Error: Matrix shapes invalid for addition")
        return None   
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    res = input.split(',')
    global rows
    rows = int(res[0])
    global columns
    columns = int(res[1])
    matrix = []
    for r in range(rows):
        matrix.append(list(input().strip().split(' ')))
    return matrix
def main():
    '''Writing inside this function'''
    # read matrix 1
    # read matrix 2
    matrix_1 = read_matrix()
    matrix_2 = read_matrix()
    print(add_matrix(matrix_1, matrix_2))
    print(mult_matrix(matrix_1, matrix_2))
if __name__ == '__main__':
    main()
