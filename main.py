def display_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            print(f"{grid[row][col]}{' ' if col != len(grid)-1 else ''}", end="")
            # print(f"{grid[row][col]}", end="")
        print()
    return

def solve(grid, colClues, rowClues):
    solved_grid = grid.copy()
    gridLen = len(grid)

    # let's find clues that fully fill out the grid on their own
    # i.e. value + space combo should yield grid length
    for colIndex, clueList in enumerate(colClues):
        if sum(clueList, len(clueList)-1) == gridLen:
            for i in range(gridLen):
                solved_grid[i][colIndex] = 1

    for rowIndex, clueList in enumerate(rowClues):
        if sum(clueList, len(clueList)-1) == gridLen:
            for i in range(gridLen):
                solved_grid[rowIndex][i] = 1
    
    

    return display_grid(solved_grid)

def main():
    print("Let's solve a nonogram :)")
    print("How large of a grid do you want? (Num of columns): ")
    gridSize = int(input())

    print(f"\nSetting up the {gridSize}x{gridSize} grid:\n")

    # Initialize lists for clues
    colClues = []
    rowClues = []

    # Valid Clues: (Clues can be digits or spaces, a space represents "1" value)
    # 1. Number of digits should be less than col
    # 2. Digits cannot have 0 (unless it is ONLY 0)
    # 3. Digit values plus space values should be at most col

    for i in range(gridSize):
        print(f"Enter the clue for Column {i + 1} (separated by spaces): ")
        clue = input().split()
        colClues.append([int(x) for x in clue if x != "-1"])

    for i in range(gridSize):
        print(f"Enter the clue for Row {i + 1} (separated by spaces): ")
        clue = input().split()
        rowClues.append([int(x) for x in clue if x != "-1"])

    print("Column clues:", colClues)
    print("Row clues:", rowClues)

    # Set up the grid as a 2D list of zeros
    grid = [["-" for _ in range(gridSize)] for _ in range(gridSize)]
    # display_grid(grid)

    solve(grid, colClues, rowClues)

main()