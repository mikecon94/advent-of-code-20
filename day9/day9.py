f = open("input", "r")
f = f.read()
inputs = [int(x) for x in f.split("\n")]

preambleLength = 25

def containsSum(queue, target):
    if max(queue) <= target / 2:
        return False
    
    for i in range(0, len(queue)):
        for j in range(i + 1, len(queue)):
            if queue[i] + queue[j] == target:
                return True
    return False

def solvePart1():
    queue = []
    for i in range(0, preambleLength):
        queue.append(inputs[i])
    
    for index in range(preambleLength, len(inputs)):
        if containsSum(queue, inputs[index]):
            queue.pop(0)
            queue.append(inputs[index])
        else:
            return str(inputs[index])

    return "1"

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())