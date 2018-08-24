"""Tic Tac Toe Game"""
def play_game(grid):
    '''To play the Tic Tac Toe Game'''
    result_winner = []
    for row in grid:
        if row[0] == row[1] == row[2]:
            result_winner.append(row[0])
    for j in range(0, 3):
        if grid[0][j] == grid[1][j] == grid[2][j]:
            result_winner.append(grid[0][j])
    if grid[0][0] == grid[1][1] == grid[2][2]:
        result_winner.append(grid[0][0])
    if grid[2][0] == grid[1][1] == grid[0][2]:
        result_winner.append(grid[2][0])
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
    matrix_1 = []
    for _ in range(0, 3):
        column = input().split(' ')
        matrix_1.append(column)
    play_game(matrix_1)
if __name__ == '__main__':
    main()
