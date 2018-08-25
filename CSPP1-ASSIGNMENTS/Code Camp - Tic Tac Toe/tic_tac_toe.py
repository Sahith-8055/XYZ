"""Tic Tac Toe Game"""
def play_game(grid):
    '''To play the Tic Tac Toe Game'''
    result_winner = []
    grid_size = len(grid[0])
    for row in grid:
        if len(set(row)) == 1:
            result_winner.append(row[0])       
    list1 = []
    for i in range(0, grid_size):
        for j in range(0, grid_size):
            list1.append(grid[j][i])
        if len(set(list1)) == 1:
            result_winner.append(grid[j][i])     
    list2 = []        
    for i in range(0, grid_size):
        list2.append(grid[i][i])
        if len(set(list2)) == 1:
            result_winner.append(grid[i][i])
    list3 = []        
    for i in range(0, grid_size):
        list3.append(grid[(grid_size - 1)-i][i])
        if len(set(list3)) == 1:
            result_winner.append(grid[(grid_size - 1)-i][i])
    result_winner = list(set(result_winner))                   
    if result_winner == []:
        print("draw")
        return None
    if len(result_winner) == 1:
        if result_winner[0] == 'x' or result_winner[0] == 'o':
            print(result_winner[0])
        else:
            print("invalid input")
        return result_winner[0]
    else:
        print("invalid game")
        return None
def main():
    '''Main function'''
    n = int(input())
    matrix_1 = []
    for _ in range(0, n):
        column = input().split(' ')
        matrix_1.append(column)
    play_game(matrix_1)
if __name__ == '__main__':
    main()
