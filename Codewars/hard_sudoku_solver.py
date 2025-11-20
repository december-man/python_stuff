puzzle = [[0,0,0,3,9,0,0,8,1],
          [6,3,0,4,0,0,0,0,0],
          [0,0,7,0,0,8,0,0,0],
          [0,0,0,0,0,0,0,0,2],
          [3,0,0,5,0,0,0,0,7],
          [1,6,0,0,0,4,0,0,0],
          [0,2,0,0,1,0,7,0,8],
          [0,0,0,0,4,0,0,0,0],
          [7,0,0,9,0,0,0,3,0]]

ans = [   [2,4,5,3,9,7,6,8,1],
          [6,3,8,4,5,1,2,7,9],
          [9,1,7,2,6,8,3,4,5],
          [5,7,4,1,3,9,8,6,2],
          [3,8,9,5,2,6,4,1,7],
          [1,6,2,8,7,4,9,5,3],
          [4,2,3,6,1,5,7,9,8],
          [8,9,1,7,4,3,5,2,6],
          [7,5,6,9,8,2,1,3,4]]

sol = puzzle
for i in range(0,9):
    for j in range(0,9):
        if not puzzle[i][j]:
            cubeset = {n for row in puzzle[3*(i//3):3*((i//3)+1)] for n in row[3*(j//3):3*((j//3)+1)]} - {0}
            rowset = {*puzzle[i]} - {0}
            colset = {row[j] for row in puzzle if row[j]} - {0}
            union = cubeset|rowset|colset
            x = {1,2,3,4,5,6,7,8,9} - union
            print(f'i,j: {(i,j)}, j//3: {j//3}, p[i][j]: {puzzle[i][j]} cube: {cubeset}, rowset: {rowset}, colset: {colset}, union: {union}, x: {x}')
            if len(x) == 1:
                print('we got a new number!')
                sol[i][j] = next(iter(x))
print(sol)

def solver(p):
    for i in range(1,10):
        for j in range(1,10):
            if not p[i][j]:
                cubeset = {n for row in p[3*(i//3):3*((i//3)+1)] for n in row[3*(j//3):3*((j//3)+1)]} - {0}
                rowset = {*p[i]} - {0}
                colset = {row[j] for row in p} - {0}
                
                
                
        