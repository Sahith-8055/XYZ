"""Matrix Operations"""
def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = [[0 for rows in range(len(matrix_1))] for columns in range(len(matrix_2[1]))]
    if len(matrix_1[0]) == len(matrix_2):
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[1])):
                for k in range(len(matrix_2)):
                    result[i][j] += int(matrix_1[i][k]) * int(matrix_2[k][j])
        return result
    print("Error: Matrix shapes invalid for mult")
    return None
def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    for i in range(len(matrix_1)):
        if len(matrix_1) == len(matrix_2) and len(matrix_1[i]) == len(matrix_2[i]):
            result = [[0 for rows in range(len(matrix_1))] for columns in range(len(matrix_1[0]))]
            result = [[int(matrix_1[i][j]) + int(matrix_2[i][j]) for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
            return result
    print("Error: Matrix shapes invalid for addition")
    return None
def read_matrix(lis):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    for _ in range(0, int(lis[0])):
        column = input().split(' ')
        if len(column) == int(lis[1]):
            matrix.append(column)
        print('Error: Invalid input for the matrix')
        return None
    return matrix
def main():
    '''Writing inside this function'''
    # read matrix 1
    # read matrix 2
    input_ = input()
    list1 = input_.split(',')
    matrix1 = read_matrix(list1)
    input_ = input()
    list2 = input_.split(',')
    matrix2 = read_matrix(list2)
    if matrix1 is not None and matrix2 is not None:
        print(add_matrix(matrix1, matrix2))
        print(mult_matrix(matrix1, matrix2))
if __name__ == '__main__':
    main()
