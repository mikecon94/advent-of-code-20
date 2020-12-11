f = open("input", "r")
inputs = f.read()
inputs = inputs.split("\n")
inputs = [int(x) for x in inputs]
inputs.sort()
inputs.append(max(inputs) + 3)

def possibleNumbers(value):
    counter = 1
    listOfNums = []
    while counter < 4:
        number = value - counter
        if number >= 0:
            listOfNums.append(value - counter)
        counter += 1
    return listOfNums


# This recursive method works backwards through the sorted list of numbers.
# For each number it checks the possible numbers that can come before it - 3 numbers below
# e.g. 9 = 6,7,8
# For each of those it checks if it is in the input and if so calls itself recursively with that number as the new root.
# The Cache stores the value of numbers already visited with 0 & 1 always being equal to 1.
# For each of the possible values in the input it will sum the value of "connections" possible.
cache = dict()
cache[0] = 1
cache[1] = 1
def populateCache(parentAdaptor):
    if cache.get(parentAdaptor) != None:
        return cache.get(parentAdaptor)
    runningTotal = 0
    for numberToCheck in possibleNumbers(parentAdaptor):
        if numberToCheck in inputs:
            runningTotal += populateCache(numberToCheck)
    cache[parentAdaptor] = runningTotal
    return runningTotal

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
    #Reverse the order to work backwards on the adaptors.
    inputs.append(0)
    inputs.sort(reverse=True)
    populateCache(max(inputs))
    return str(max(cache.values()))

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())