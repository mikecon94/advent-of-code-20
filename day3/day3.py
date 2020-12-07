f = open("input", "r")

columns = 0
rows = 0

map = []
for line in f.readlines():
    row = []
    for char in line:
        if(char != "\n"):
            row.append(char)
    map.append(row)
rows = len(map)
columns = len(map[0])


def countTreesOnSlope(rowSlope, columnSlope):
    noOfTrees = 0
    tobogganColumn = 0
    tobogganRow = 0
    while tobogganRow < rows:
        if map[tobogganRow][tobogganColumn] == "#":
            noOfTrees += 1
        tobogganRow += rowSlope
        
        tobogganColumn += columnSlope
        if tobogganColumn >= columns:
            tobogganColumn = tobogganColumn - columns
    return noOfTrees

def solvePart2():
    result = 1
    result = countTreesOnSlope(1, 1)
    result *= countTreesOnSlope(1, 3)
    result *= countTreesOnSlope(1, 5)
    result *= countTreesOnSlope(1, 7)
    result *= countTreesOnSlope(2, 1)
    return str(result)

print("Part 1: " + str(countTreesOnSlope(1, 3)))
print("Part 2: " + solvePart2())