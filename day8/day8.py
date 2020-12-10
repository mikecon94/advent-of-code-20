class Computer:

    def __init__(self, instructions, accValue, instructionIndex):
        self.instructions = instructions
        self.accValue = accValue
        self.instructionIndex = instructionIndex

    def acc(self, value):
        self.accValue += value
        self.instructionIndex += 1

    def jmp(self, value):
        self.instructionIndex += value

    def nop(self, value):
        self.instructionIndex += 1

    def runCurrentInstruction(self):
        switcher = {
            "jmp": self.jmp,
            "acc": self.acc,
            "nop": self.nop
        }
        func = switcher.get(self.instructions[self.instructionIndex][0], "INVALID OPERATION")
        return func(self.instructions[self.instructionIndex][1])

    #Returns True if ran until completion, otherwise returns False when
    #Same instruction is hit twice.
    def run(self):
        instructionsRan = [False] * len(self.instructions)
        instructionRepeated = False
        while True:
            if self.instructionIndex == len(self.instructions):
                break
            if instructionsRan[self.instructionIndex] == True:
                instructionRepeated = True
                break
            instructionsRan[self.instructionIndex] = True
            self.runCurrentInstruction()
        return not instructionRepeated

f = open("input", "r")
lines = f.read()
linesArray = lines.split("\n")
inputInstructions = []
for line in linesArray:
    operation = line.split(" ")[0]
    value = int(line.split(" ")[1])
    instruction = [operation, value]
    inputInstructions.append(instruction)

def deepCopy():
    newInstructions = []
    for instruction in inputInstructions:
        newInstructions.append([instruction[0], instruction[1]])
    return newInstructions

def solvePart1():
    computer = Computer(inputInstructions, 0, 0)
    computer.run()
    return str(computer.accValue)

def solvePart2():
    # Loop round each instruction, changing them one by one.
    for i in range(0, len(inputInstructions)):
        # Deep Copy of instructions (including containing value)
        # So we can revert to original input list each time.
        instructionsCopy = deepCopy()
        if instructionsCopy[i][0] == "nop":
            instructionsCopy[i][0] = "jmp"
        elif instructionsCopy[i][0] == "jmp":
            instructionsCopy[i][0] = "nop"
        else:
            continue

        computer = Computer(instructionsCopy, 0, 0)
        if computer.run():
            return str(computer.accValue)
    return "0"
       
    # computer = Computer(inputInstructions, 0, 0)
    # instructionsRan = [False] * len(inputInstructions)
    # wrongInstruction = False
    # while True:
    #     if instructionsRan[computer.instructionIndex] == True:
    #         break
    #     if computer.instructionIndex == len(computer.instructions):
    #         break
    #     instructionsRan[computer.instructionIndex] = True
    #     computer.runCurrentInstruction()
    # return str(computer.accValue)

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())