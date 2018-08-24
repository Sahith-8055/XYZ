def PlayGame(grid):
    Winner = []
    for row in grid:
        if row[0] == row[1] == row[2]:
            Winner.append(row[0])
    for j in range(0,3):
        if grid[0][j] == grid[1][j] == grid[2][j]:
            Winner.append(grid[0][j])
    if grid[0][0] == grid[1][1] == grid[2][2]:
        Winner.append(grid[0][0])
    if grid[2][0] == grid[1][1] == grid[0][2]:
        Winner.append(grid[2][0])
    if Winner == []:
        print("draw")
        return None
    if len(Winner) == 1:
        if Winner[0] == 'x' or Winner[0] == 'o':
            print(Winner[0])
        else:
            print("invalid input")
        return Winner[0]
    else:
        print("invalid game")
        return None
def main():
    matrix_1 = []
    for _ in range(0,3):
        column = input().split(' ')
        matrix_1.append(column)
    PlayGame(matrix_1)    
if __name__ == '__main__':
    main()