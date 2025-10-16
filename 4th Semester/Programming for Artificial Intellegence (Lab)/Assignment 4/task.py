def print_grid(grid):
    for i in grid:
        print(" ".join("Q" if c else "." for c in i))
    print()

def safe(grid,row,col,n):
    for i in range(row):
        if grid[i][col]:
            return False
    i,j=row-1, col-1
    while i>=0 and j>=0:
        if grid[i][j]:
            return False
        i-=1
        j-=1
    i,j=row-1, col+1
    while i>=0 and j<n:
        if grid[i][j]:
            return False
        i-=1
        j+=1
    return True

def solve(grid,row,n,outcome):
    if row==n:
        outcome.append([r[:] for r in grid])
        return
    for col in range(n):
        if safe(grid, row, col, n):
            grid[row][col] = 1
            solve(grid, row + 1, n, outcome)
            grid[row][col] = 0

n=int(input("Enter the number of queens: "))
board=[[0]*n for _ in range(n)]
outcome=[]
solve(board,0,n,outcome)

print(f"Total solutions for N={n}: {len(outcome)}\n")
count=1
for sol in outcome:
    print(f"Solution {count}:")
    print_grid(sol)
    count+=1