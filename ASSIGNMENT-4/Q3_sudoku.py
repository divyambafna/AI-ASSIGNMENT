grid = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return i,j
    return None

def valid(grid,num,pos):
    row,col = pos

    for i in range(9):
        if grid[row][i]==num and col!=i:
            return False

    for i in range(9):
        if grid[i][col]==num and row!=i:
            return False

    box_x = col//3
    box_y = row//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if grid[i][j]==num and (i,j)!=pos:
                return False

    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    row,col = find

    for num in range(1,10):
        if valid(grid,num,(row,col)):
            grid[row][col]=num

            if solve(grid):
                return True

            grid[row][col]=0

    return False

solve(grid)

for row in grid:
    print(row)