def display_grid(grid):
    print()
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

    # Column Clues
    for colIndex, clueList in enumerate(colClues):
        if sum(clueList, len(clueList)-1) == gridLen:
            rowIndex = 0
            for clue in clueList:
                # fill out 1 value for clue
                for i in range(rowIndex, rowIndex+clue):
                    solved_grid[i][colIndex] = 1
                
                # fill out 0 for single space between clues
                rowIndex = rowIndex+clue
                if rowIndex < gridLen:
                    solved_grid[rowIndex][colIndex] = 0
                    rowIndex = rowIndex+1

    # Row Clues
    for rowIndex, clueList in enumerate(rowClues):
        if sum(clueList, len(clueList)-1) == gridLen:
            colIndex = 0
            for clue in clueList:
                # fill out 1 value for clue
                for i in range(colIndex, colIndex+clue):
                    solved_grid[rowIndex][i] = 1
                
                # fill out 0 for single space between clues
                colIndex = colIndex+clue
                if colIndex < gridLen:
                    solved_grid[rowIndex][colIndex] = 0
                    colIndex = colIndex+1

    return display_grid(solved_grid)

def main():
    print("Let's solve a nonogram :)")
    # print("How large of a grid do you want? (Num of columns): ")
    # gridSize = int(input())
    gridSize = 15

    print(f"\nSetting up the {gridSize}x{gridSize} grid:\n")

    # Initialize lists for clues
    colClues = []
    rowClues = []

    # Valid Clues: (Clues can be digits or spaces, a space represents "1" value)
    # 1. Number of digits should be less than col
    # 2. Digits cannot have 0 (unless it is ONLY 0)
    # 3. Digit values plus space values should be at most col

    # for i in range(gridSize):
    #     print(f"Enter the clue for Column {i + 1} (separated by spaces): ")
    #     clue = input().split()
    #     colClues.append([int(x) for x in clue if x != "-1"])

    # for i in range(gridSize):
    #     print(f"Enter the clue for Row {i + 1} (separated by spaces): ")
    #     clue = input().split()
    #     rowClues.append([int(x) for x in clue if x != "-1"])

    colClues = [[11, 3], [1, 6, 2], [2], [1, 1, 2, 2], [3, 2], [4, 1, 2], [4, 3, 22], [4, 1, 2], [3, 2], [1, 1, 2], [2, 1], [1, 2, 2], [9, 2], [6, 1, 3], [6, 7]]
    rowClues = [[2, 7, 4], [1, 5, 3], [1, 5, 3], [1, 3, 3], [2, 3], [2, 1, 1, 1, 3], [2, 3, 1], [2, 1, 1], [3, 4], [12, 1], [1, 8, 1], [1], [1, 2], [2, 1, 1, 4], [2, 1, 1, 5]]

    print("Column clues:", colClues)
    print("Row clues:", rowClues)

    # Set up the grid as a 2D list of zeros
    grid = [["-" for _ in range(gridSize)] for _ in range(gridSize)]
    # display_grid(grid)

    solve(grid, colClues, rowClues)

main()