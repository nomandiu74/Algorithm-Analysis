def issafe(grid, x, y, n):
    # Check the column for any queen
    for row in range(n):
        if grid[row][y] == 1:
            return False

    # Check the upper left diagonal
    row = x
    col = y
    while row >= 0 and col >= 0:
        if grid[row][col] == 1:
            return False
        row -= 1
        col -= 1

    # Check the upper right diagonal
    row = x
    col = y
    while row >= 0 and col < n:
        if grid[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def nqueen(grid, x, n):
    # Base case: when x equals n, a valid solution has been found
    if x == n:
        # Print the solution in a grid format
        for row in grid:
            print(row)
        print()  # Print a newline after each solution
        return

    # Try placing a queen in each column of row x
    for y in range(n):
        if issafe(grid, x, y, n):
            grid[x][y] = 1  # Place the queen
            nqueen(grid, x + 1, n)  # Recur to place rest of the queens
            grid[x][y] = 0  # Backtrack


n = int(input("Enter the number of queens: "))
if n in [4, 8, 16, 32]:
    grid = [[0 for j in range(n)] for i in range(n)]
    nqueen(grid, 0, n)
else:
    print("No solution")
