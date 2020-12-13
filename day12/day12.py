f = open("input", "r")
lines = f.read()
lines = lines.split("\n")

class Instruction:
    def __init__(self, direction, value):
        self.direction = direction
        self.value = int(value)

    def print(self):
        print("DIRECTION: " + self.direction + " VALUE: " + str(self.value))

class Ship:

    directions = {'N': { 'x': 0, 'y': 1, 90: 'E', 180: 'S', 270: 'W'},
                  'S': { 'x': 0, 'y': -1,90: 'W', 180: 'N', 270: 'E'},
                  'W': { 'x': -1, 'y': 0,90: 'N', 180: 'E', 270: 'S'},
                  'E': { 'x': 1, 'y': 0, 90: 'S', 180: 'W', 270: 'N'}}

    def __init__(self, facing = "E", xPos = 0, yPos = 0):
        self.facing = facing
        self.xPos = xPos
        self.yPos = yPos

    def runInstruction(self, instruction: Instruction):
        # instruction.print()
        # print("FACING: " + str(self.facing))
        if instruction.direction == 'F':
            self.xPos += self.directions.get(self.facing).get('x') * instruction.value
            self.yPos += self.directions.get(self.facing).get('y') * instruction.value
        elif instruction.direction in self.directions:
            self.xPos += self.directions.get(instruction.direction).get('x') * instruction.value
            self.yPos += self.directions.get(instruction.direction).get('y') * instruction.value
        if instruction.direction in ['L', 'R']:
            if instruction.direction == 'L':
                if instruction.value == 90:
                    instruction.value = 270
                elif instruction.value == 270:
                    instruction.value = 90
            self.facing = self.directions.get(self.facing).get(instruction.value) 
            # print("FACING: " + str(self.facing))

    def calculateManhattanDistance(self):
        return abs(self.xPos) + abs(self.yPos)

instructions = []
for line in lines:
    instruction = Instruction(line[0], line[1:])
    instructions.append(instruction)

def solvePart1():
    ship = Ship()
    for instruction in instructions:
        ship.runInstruction(instruction)
    return str(ship.calculateManhattanDistance())

def solvePart2():
    return "2"

#1834 is too high
print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())
