# The pocket dimension contains an infinite 3-dimensional grid.
# At every integer 3-dimensional coordinate (x,y,z),
# there exists a single cube which is either active or inactive.
# # = active
# . = inactive
# Input is layer of z=0
# 26 Neighbours - all cubes where any coordinate differs by 1.
# Simulataneously change state.

# If cube is active and EXACTLY 2 or 3 neighbours are active the cube remains active.
# Otherwise it becomes inactive.

# If cube is inactive but exactly 3 neighbours are active the cube becomes active.
import json


f = open("input", "r")
f = f.read()
startingLayer = dict()
for lineIndex, line in enumerate(f.split("\n")):
    row = dict()
    for index, cube in enumerate(line):
        row[index] = cube
    startingLayer[lineIndex] = row

def getNewCube(minZ, maxZ, minY, maxY, minX, maxX):
    # print("CREATING NEW CUBE")
    # print(minZ, maxZ, minY, maxY, minX, maxX)
    newCube = dict()
    for z in range(minZ, maxZ + 1):
        layer = dict()
        for y in range(minY, maxY + 1):
            row = dict()
            for x in range(minX, maxX + 1):
                row[x] = "."
            layer[y] = row
        newCube[z] = layer
    return newCube

def countActiveCubes(cube):
    total = 0
    for z in range(min(cube), max(cube) + 1):
        for y in range(min(cube[0]), max(cube[0]) + 1):
            for x in range(min(cube[0][0]), max(cube[0][0]) + 1):
                if cube[z][y][x] == "#":
                    total += 1
    return total

def printCube(cube):
    for z in range(min(cube), max(cube) + 1):
        print("Z = " + str(z))
        for y in range(min(cube[0]), max(cube[0]) + 1):
            for x in range(min(cube[0][0]), max(cube[0][0]) + 1):
                print(cube[z][y][x], end='')
            print()
        print()

def getCell(cube, z, y, x):
    if cube.get(z, None) != None:
        if cube.get(z).get(y, None) != None:
            if cube.get(z).get(y).get(x, None) != None:
                return cube.get(z).get(y).get(x)
    return "."

# This appears to be working as expected
def countActiveNeighbours(pocketCube, zIndex, yIndex, xIndex):
    # print(zIndex, yIndex, xIndex)
    # print(getCell(pocketCube, zIndex, yIndex, xIndex))
    totalCounted = 0
    total = 0
    for z in range(zIndex - 1, zIndex + 2):
        for y in range(yIndex - 1, yIndex + 2):
            for x in range(xIndex - 1, xIndex + 2):
                if z != zIndex or y != yIndex or x != xIndex:
                    totalCounted += 1
                    if getCell(pocketCube, z, y, x) == "#":
                        total += 1
    assert(totalCounted == 26)
    return total

def solvePart1():
    pocketCube = dict()
    pocketCube[0] = startingLayer

    cycleCount = 0
    while cycleCount < 1:
        # This may not be necesarry and we can simply iterate over existing cube anyway...
        # thisCycleCube = getNewCube(min(pocketCube)      - 1, max(pocketCube) + 1, 
        #                            min(pocketCube[0])       - 1, max(pocketCube[0]) + 1,
        #                            min(pocketCube[0][0])    - 1, max(pocketCube[0][0]) + 1)    
        printCube(pocketCube)
        thisCycleCube = dict()
        for z in range(min(pocketCube) - 1, max(pocketCube) + 2):
            layer = dict()
            for y in range(min(pocketCube[0]) - 1, max(pocketCube[0]) + 2):
                row = dict()
                for x in range(min(pocketCube[0][0]) - 1, max(pocketCube[0][0]) + 2):
                    # print(z, y, x, getCell(pocketCube, z, y, x))
                    currentCell = getCell(pocketCube, z, y, x)
                    activeNeighbours = countActiveNeighbours(pocketCube, z, y, x)
                    if currentCell == ".":
                        if activeNeighbours == 3:
                            currentCell = "#"
                    elif currentCell == "#":
                        if activeNeighbours == 2 or activeNeighbours == 3:
                            currentCell = "."
                    row[x] = currentCell
                layer[y] = row
                # print(layer)
            thisCycleCube[z] = layer
            # print(z, thisCycleCube)

        # print(thisCycleCube)
        pocketCube = thisCycleCube
        cycleCount += 1
    # printCube(pocketCube)

    # print(pocketCube)
    return str(countActiveCubes(pocketCube))

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())