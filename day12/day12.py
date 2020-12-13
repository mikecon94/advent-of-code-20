import math

f = open("input", "r")
lines = f.read()
lines = lines.split("\n")

class Instruction:
    def __init__(self, direction, value):
        self.direction = direction
        self.value = int(value)

    def print(self):
        print("INSTRUCTION - DIRECTION: " + self.direction + " VALUE: " + str(self.value))

class Ship:

    directions = {'N': { 'x': 0, 'y': 1, 90: 'E', 180: 'S', 270: 'W'},
                  'S': { 'x': 0, 'y': -1,90: 'W', 180: 'N', 270: 'E'},
                  'W': { 'x': -1, 'y': 0,90: 'N', 180: 'E', 270: 'S'},
                  'E': { 'x': 1, 'y': 0, 90: 'S', 180: 'W', 270: 'N'}}

    def __init__(self, facing = "E", xPos = 0, yPos = 0, waypointX = 10, waypointY = 1):
        self.facing = facing
        self.xPos = xPos
        self.yPos = yPos
        self.waypointX = waypointX
        self.waypointY = waypointY

    def runInstruction(self, instruction: Instruction):
        # instruction.print()
        # print("FACING: " + str(self.facing))
        if instruction.direction == 'F':
            self.xPos += self.directions.get(self.facing).get('x') * instruction.value
            self.yPos += self.directions.get(self.facing).get('y') * instruction.value
        elif instruction.direction in self.directions:
            self.xPos += self.directions.get(instruction.direction).get('x') * instruction.value
            self.yPos += self.directions.get(instruction.direction).get('y') * instruction.value
        if instruction.direction == 'R':
            self.facing = self.directions.get(self.facing).get(instruction.value) 
            # print("FACING: " + str(self.facing))

    def runInstructionUsingWaypoint(self, instruction: Instruction):
        # print("SHIP: " + str(self.xPos) + ", " + str(self.yPos) + " WAYPOINT: " + str(self.waypointX) + "," + str(self.waypointY))
        # instruction.print()
        # Move ship to Waypoint X times.
        if instruction.direction == 'F':
            self.xPos += self.waypointX * instruction.value
            self.yPos += self.waypointY * instruction.value
        elif instruction.direction in self.directions:
            self.waypointX += self.directions.get(instruction.direction).get('x') * instruction.value
            self.waypointY += self.directions.get(instruction.direction).get('y') * instruction.value
        elif instruction.direction == 'R':
            self.rotateWaypointClockwiseAroundShip(instruction.value)

    def rotateWaypointClockwiseAroundShip(self, angle):
        newX = self.waypointX
        newY = self.waypointY
        if angle == 90:
            tempX = newX
            newX = newY
            newY = tempX * -1
        elif angle == 180:
            newX *= -1
            newY *= -1
        elif angle == 270:
            tempX = newX
            newX = newY * -1
            newY = tempX
        self.waypointX = newX
        self.waypointY = newY

    def calculateManhattanDistance(self):
        return abs(self.xPos) + abs(self.yPos)

instructions = []
for line in lines:
    instruction = Instruction(line[0], line[1:])
    if instruction.direction == "L":
        instruction.direction = "R"
        if instruction.value == 90:
            instruction.value = 270
        elif instruction.value == 270:
            instruction.value = 90
    instructions.append(instruction)

def solvePart1():
    ship = Ship()
    for instruction in instructions:
        ship.runInstruction(instruction)
    return str(ship.calculateManhattanDistance())

def solvePart2():
    ship = Ship()
    for instruction in instructions:
        ship.runInstructionUsingWaypoint(instruction)
    return str(ship.calculateManhattanDistance())

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())
