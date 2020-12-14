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
    
    def runInstructionWithDecoder(self, instruction):
        if instruction.type == "mask":
            self.mask = instruction.value
        elif instruction.type == "mem":
            newAddressFloats = self.applyBitmaskWithFloats(self.mask, instruction.address)
            # Write instruction.value to all addresses possible.
            for address in self.getAddresses(newAddressFloats, 0):
                self.memory[address] = instruction.value
        self.index += 1

    # Recursive function that returns all permutations of an address with FLOATS (X) in.
    def getAddresses(self, initialAddress, index):
        listOfAddresses = []
        if index == len(initialAddress):
            listOfAddresses.append(initialAddress)
        else:
            if initialAddress[index] == "X":
                newAddress = initialAddress[:index] + "0" + initialAddress[index +1:]
                listOfAddresses += self.getAddresses(newAddress, index+1)
                newAddress = initialAddress[:index] + "1" + initialAddress[index +1:]
                listOfAddresses += self.getAddresses(newAddress, index+1)
            else:
                listOfAddresses += self.getAddresses(initialAddress, index+1)
        return listOfAddresses

    def applyBitmaskWithFloats(self, mask, value):
        value = bin(value)[2:].rjust(36, '0')
        newValue = ''
        for index, bit in enumerate(mask):
            if bit == "0":
                newValue += value[index]
            elif bit == "1":
                newValue += "1"
            else:
                newValue += bit
        return newValue

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
    computer = Computer(instructions)
    for instruction in instructions:
        computer.runInstructionWithDecoder(instruction)
    return str(sum(computer.memory.values()))

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())