f = open("input", "r")
f = f.read()
inputs = [int(x) for x in f.split("\n")]

PREAMBLE_LENGTH = 25

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
    for i in range(0, PREAMBLE_LENGTH):
        queue.append(inputs[i])
    
    for index in range(PREAMBLE_LENGTH, len(inputs)):
        if containsSum(queue, inputs[index]):
            queue.pop(0)
            queue.append(inputs[index])
        else:
            return str(inputs[index])
    return "FAIL"

def solvePart2():
    target = int(solvePart1())
    contiguousNumbers = []
    for index in range(0, len(inputs)):
        contiguousNumbers = [inputs[index]]
        resultFound = False
        counter = 0
        while not resultFound:
            sumOfCurrentNums = sum(contiguousNumbers)
            if sumOfCurrentNums == target:
                resultFound = True
                break
            elif sumOfCurrentNums > target:
                resultFound = False
                break
            else:
                resultFound = False
                counter += 1
                contiguousNumbers.append(inputs[index + counter])
        if resultFound:
            return str(max(contiguousNumbers) + min(contiguousNumbers))

    return "FAIL"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())