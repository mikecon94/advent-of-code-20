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

def countOccupiedVisibleSeats(layout, seatRow, seatColumn):
    # # We remove all floor spaces and then count as normal.
    # # This didn't work as it changed the grid layout, e.g. moving elements closer.
    # newLayout = deepCopyLayout(layout)
    # for rowIndex, row in reversed(list(enumerate(newLayout))):
    #     for columnIndex, seat in reversed(list(enumerate(row))):
    #         # print("ROW: " + str(row) + " Seat: " + str(seat))
    #         if seat == ".":
    #             # print("DELETING ELEMENT: " + str(rowIndex) + " Col: " + str(columnIndex))
    #             del newLayout[rowIndex][columnIndex]
    # print(newLayout)
    # return countOccupiedAdjacentSeats(newLayout, seatRow, seatColumn)
    count = 0
    count += checkVisibleOccupiedSeatRight(layout, seatRow, seatColumn)
    count += checkVisibleOccupiedSeatLeft(layout, seatRow, seatColumn)
    count += checkVisibleOccupiedSeatAbove(layout, seatRow, seatColumn)
    count += checkVisibleOccupiedSeatBelow(layout, seatRow, seatColumn)
    count += checkVisibleOccupiedSeatUpRight(layout, seatRow, seatColumn)
    count += checkVisibleOccupiedSeatUpLeft(layout, seatRow, seatColumn)
    count += checkVisibleOccupiedSeatDownRight(layout, seatRow, seatColumn)
    count += checkVisibleOccupiedSeatDownLeft(layout, seatRow, seatColumn)
    return count

# print("SEAT: " + str(seat) + " ROW: " + str(seatRow + indexCount) + " COL: " + str(seatColumn + indexCount))
def checkVisibleOccupiedSeatDownLeft(layout, seatRow, seatColumn):
    #Seat Row goes up, seat column goes down.
    rowIndexDelta = 1
    colIndexDelta = -1
    seat = layout[seatRow][seatColumn]
    while (seatRow + rowIndexDelta) < len(layout) and (seatColumn + colIndexDelta) >= 0:
        seat = layout[seatRow + rowIndexDelta][seatColumn + colIndexDelta]
        if seat == "#":
            return 1
        if seat == "L":
            return 0
        rowIndexDelta += 1
        colIndexDelta -= 1
    return 0


def checkVisibleOccupiedSeatUpRight(layout, seatRow, seatColumn):
    #Seat Row goes down, seat column goes up.
    rowIndexDelta = -1
    colIndexDelta = 1
    seat = layout[seatRow][seatColumn]
    while (seatRow + rowIndexDelta) >= 0 and (seatColumn + colIndexDelta) < len(layout[seatRow + rowIndexDelta]):
        seat = layout[seatRow + rowIndexDelta][seatColumn + colIndexDelta]
        if seat == "#":
            return 1
        if seat == "L":
            return 0
        rowIndexDelta -= 1
        colIndexDelta += 1
    return 0

def checkVisibleOccupiedSeatUpLeft(layout, seatRow, seatColumn):
    indexCount = -1
    seat = layout[seatRow][seatColumn]
    while (seatRow + indexCount) >= 0 and (seatColumn + indexCount) >= 0:
        seat = layout[seatRow + indexCount][seatColumn + indexCount]
        if seat == "#":
            return 1
        if seat == "L":
            return 0
        indexCount -= 1
    return 0

def checkVisibleOccupiedSeatDownRight(layout, seatRow, seatColumn):
    indexCount = 1
    seat = layout[seatRow][seatColumn]
    while (seatRow + indexCount) < len(layout) and (seatColumn + indexCount) < len(layout[seatRow]):
        seat = layout[seatRow + indexCount][seatColumn + indexCount]
        if seat == "#":
            return 1
        if seat == "L":
            return 0
        indexCount += 1
    return 0

def checkVisibleOccupiedSeatBelow(layout, seatRow, seatColumn):
    for rowIndex in range(seatRow + 1, len(layout)):
        if layout[rowIndex][seatColumn] == "#":
            return 1
        elif layout[rowIndex][seatColumn] == "L":
            return 0
    return 0

def checkVisibleOccupiedSeatAbove(layout, seatRow, seatColumn):
    for rowIndex in range(1, seatRow + 1):
        # print("SEAT: " + str(layout[seatRow - rowIndex][seatColumn]) + " ROW: " + str(seatRow - rowIndex) + " COL: " + str(seatColumn))
        if layout[seatRow - rowIndex][seatColumn] == "#":
            return 1
        elif layout[seatRow - rowIndex][seatColumn] == "L":
            return 0
    return 0

def checkVisibleOccupiedSeatRight(layout, seatRow, seatColumn):
    for columnIndex in range(seatColumn + 1, len(layout[seatRow])):
        if layout[seatRow][columnIndex] == "#":
            return 1
        elif layout[seatRow][columnIndex] == "L":
            return 0
    return 0

def checkVisibleOccupiedSeatLeft(layout, seatRow, seatColumn):
    for columnIndex in range(1, seatColumn + 1):
        if layout[seatRow][seatColumn - columnIndex] == "#":
            return 1
        elif layout[seatRow][seatColumn - columnIndex] == "L":
            return 0
    return 0

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

def printLayout(layout):
    for row in layout:
        printLine = ""
        for seat in row:
            printLine += seat
        print(printLine)
    print("")

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
    # Similar to part 1 but instead of adjacent seats we check first visible seat.
    # And they now allow 5 or more occupied seats.
    # Empty seats that see no ocupied seats become occupied.
    # Occupied Seats that see 5 or more occupied seats become empty.

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
                    if countOccupiedVisibleSeats(layout, rowIndex, columnIndex) == 0:
                        changeMade = True
                        newLayout[rowIndex][columnIndex] = "#"
                elif seat == "#":
                    # If 5 or more seats occupied then make it empty
                    if countOccupiedVisibleSeats(layout, rowIndex, columnIndex) >= 5:
                        changeMade = True
                        newLayout[rowIndex][columnIndex] = "L"
                # Skip Floor seats
        layout = newLayout
        # printLayout(layout)
    return str(countOccupiedSeats(layout))

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())