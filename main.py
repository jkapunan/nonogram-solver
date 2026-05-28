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

