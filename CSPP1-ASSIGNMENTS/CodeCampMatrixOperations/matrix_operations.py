"""Matrix Operations"""
def mult_matrix(matrix1, matrix2):
    '''
       check if the matrix1 columns = matrix2 rows
       mult the matrices and return the result matrix
       print an error message if the matrix shapes are not valid for mult
       and return None
       error message should be "Error: Matrix shapes invalid for mult"
    '''
    m1_rows = len(matrix1)
    m1_columns = len(matrix2[1])
    m2_rows = len(matrix2) 
    if len(matrix1) == len(matrix2[0]) and len(matrix1[0]) == len(matrix2):
        result = [[0 for row in range(len(matrix1))] for col in range(len(matrix2[1]))]
        for i in range(m1_rows):
            for j in range(m1_columns):
                for k in range(m2_rows):
                    result[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
        return result
    print("Error: Matrix shapes invalid for mult")
    return None
def add_matrix(matrix1, matrix2):
    '''
       check if the matrix shapes are similar
       add the matrices and return the result matrix
       print an error message if the matrix shapes are not valid for addition
       and return None
       error message should be "Error: Matrix shapes invalid for addition"
    '''
    for i in range(len(matrix1)):
        if len(matrix1) == len(matrix2) and len(matrix1[i]) == len(matrix2[i]):
            result = [[0 for row in range(len(matrix1))] for col in range(len(matrix2[0]))]
            result = [[int(matrix1[i][j]) + int(matrix2[i][j])for j in range(len(matrix1[0]))]for i in range(len(matrix1))]
            return result
    print('Error: Matrix shapes invalid for addition')
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
        col = input().split(' ')
        if len(col) == int(lis[1]):
            matrix.append(col)
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix
def main():
    '''Writing inside this function'''
    input_inp = input()
    list1 = input_inp.split(',')
    matrix_1 = read_matrix(list1)
    input_inp = input()
    list2 = input_inp.split(',')
    matrix_2 = read_matrix(list2)
    if matrix_1 is not None and matrix_2 is not None:
        print(add_matrix(matrix_1, matrix_2))
        print(mult_matrix(matrix_1, matrix_2))
if __name__ == '__main__':
    main()
