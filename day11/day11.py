f = open("input", "r")
f = f.read()
f = f.split("\n")

initialLayout = []
for line in f:
    input = []
    for char in line:
        input.append(char)
    initialLayout.append(input)

# Decisions are based on number of occupied seats adjacent to the seat.
# Up, Down, Left, Right and Diagonal.
# initialLayout[0] = Row 0
# initialLayout[0][1] = Row 0, Column 1
# [[00, 01, 02]     (-1, -1)    (-1, 0)     (-1, +1)
#  [10, 11, 12]     ( 0, -1)    ( 0, 0)     ( 0, +1)
#  [20, 21, 22]]    (+1, -1)    (+1, 0)     (+1, +1)
# L = Empty Seat
# . = Floor Space
# # = Taken Seat
# If a seat is empty and there are no occupied seats adjacent to it, seat becomes occupied
# If a seat is occupied AND 4 or more seats adjacent to it are also occupied, teh seat becomes empty.
# Otherwise state does not change.
# Floor does not change.

def countOccupiedAdjacentSeats(layout, seatRow, seatColumn):
    count = 0
    for column in range(-1, 2):
        for row in range(-1, 2):
            # Ignore 0,0 as this is the current seat
            if column != 0 or row != 0:
                newRow = seatRow + row
                newColumn = seatColumn + column
                if (newRow >= 0 and newRow < len(layout)
                        and newColumn >= 0 and newColumn < len(layout[newRow])):
                    if layout[newRow][newColumn] == "#":
                        count += 1
    return count

def countOccupiedSeats(layout):
    count = 0
    for row in layout:
        for seat in row:
            if seat == "#":
                count += 1
    return count

def deepCopyLayout(layout):
    newLayout = []
    for row in layout:
        newRow = []
        for seat in row:
            newRow.append(seat)
        newLayout.append(newRow)
    return newLayout

def solvePart1():
    # Loop round until no changes are made (state has stabilised)
    layout = deepCopyLayout(initialLayout)
    changeMade = True
    while changeMade:
        changeMade = False
        newLayout = deepCopyLayout(layout)
        # Loop round each seat making changes where required.
        for rowIndex, row in enumerate(layout):
            for columnIndex, seat in enumerate(row):
                if seat == "L":
                    # If no seats occupied then make it occupied
                    if countOccupiedAdjacentSeats(layout, rowIndex, columnIndex) == 0:
                        changeMade = True
                        newLayout[rowIndex][columnIndex] = "#"
                elif seat == "#":
                    # If 4 or more seats occupied then make it empty
                    if countOccupiedAdjacentSeats(layout, rowIndex, columnIndex) >= 4:
                        changeMade = True
                        newLayout[rowIndex][columnIndex] = "L"
                # Skip Floor seats
        layout = newLayout
    return str(countOccupiedSeats(layout))

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())