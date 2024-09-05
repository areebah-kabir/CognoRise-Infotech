def print_grid(grid):
    for row in grid:
        print(row)

def is_safe(grid, row, col, num):
    # Check if 'num' is not in the current row and column
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    # Check if 'num' is not in the current 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid):
    # Find an empty cell (represented by 0)
    empty_cell = [(row, col) for row in range(9) for col in range(9) if grid[row][col] == 0]
    if not empty_cell:
        return True  # Puzzle solved if no empty cell is found
    row, col = empty_cell[0]

    # Try placing numbers from 1 to 9
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Backtrack

    return False

def get_sudoku_from_user():
    print("Please enter your Sudoku puzzle row by row.")
    print("Use 0 for empty cells.")
    grid = []
    for i in range(9):
        while True:
            row_input = input(f"Enter 9 numbers for row {i + 1} (0 for empty cells): ")
            row = [int(num) for num in row_input if num.isdigit()]
            if len(row) == 9:
                grid.append(row)
                break
            else:
                print("Invalid input. Please enter exactly 9 digits.")
    return grid

# Get the Sudoku puzzle from the user
sudoku_grid = get_sudoku_from_user()

# Solve and print the solution if possible
if solve_sudoku(sudoku_grid):
    print("Solved Sudoku grid:")
    print_grid(sudoku_grid)
else:
    print("No solution exists for the given Sudoku.")
