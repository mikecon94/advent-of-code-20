class Instruction:
    def __init__(self, type, value, address = -1):
        self.type = type
        if type == "mem":
            self.value = int(value)
            self.address = int(address)
        elif type == "mask":
            self.value = value
    
    def print(self):
        if self.type == "mask":
            print("INSTR MASK: " + str(self.value))
        elif self.type == "mem":
            print("INSTR MEM: [" + str(self.address) + "] VALUE: " + str(self.value))

class Computer:
    def __init__(self, instructions, mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"):
        self.instructions = instructions
        self.mask = mask
        self.memory = dict()
        self.index = 0

    def runCurrentInstruction(self):
        instruction = self.instructions[self.index]
        if instruction.type == "mask":
            self.mask = instruction.value
        elif instruction.type == "mem":
            self.memory[instruction.address] = self.applyBitmask(self.mask, instruction.value)
        self.index += 1
    
    def applyBitmask(self, mask, value):
        value = bin(value)[2:].rjust(36, '0')
        newValue = ''
        for index, bit in enumerate(mask):
            if bit == "X":
                newValue += value[index]
            else:
                newValue += bit
        return int(newValue, 2)

    def runInstructions(self):
        for instruction in self.instructions:
            self.runCurrentInstruction()

    def print(self):
        print("COMPUTER: ", self.mask, self.memory, self.index)

f = open("input", "r")
lines = f.read().split("\n")

instructions = []
for line in lines:
    lineParts = line.split(" = ")
    value = lineParts[1]
    if lineParts[0] == "mask":
        instruction = Instruction("mask", value)
    else:
        type = "mem"
        address = lineParts[0][4:-1]
        instruction = Instruction("mem", value, address)
    instructions.append(instruction)        

# [instruction.print() for instruction in instructions]

def solvePart1():
    computer = Computer(instructions)
    computer.runInstructions()
    return str(sum(computer.memory.values()))

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())