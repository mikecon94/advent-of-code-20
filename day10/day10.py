f = open("input", "r")
inputs = f.read()
inputs = inputs.split("\n")
inputs = [int(x) for x in inputs]
inputs.sort()
inputs.append(max(inputs) + 3)

def solvePart1():
    lastNumber = 0
    countOfOneJump = 0
    countOfThreeJump = 0
    for input in inputs:
        if input - lastNumber == 1:
            countOfOneJump += 1
        if input - lastNumber == 3:
            countOfThreeJump += 1
        lastNumber = input
    return str(countOfOneJump * countOfThreeJump)

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())