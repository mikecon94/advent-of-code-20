startingNumbers = [0,6,1,7,2,19,20]

def playGameUpTo(turnNumber):
    turn = 1
    # Key = Number, Value = Turn Last Spoken
    # This should have been other way round - turn/index = value
    lastSpoken = dict()
    for index, num in enumerate(startingNumbers):
        lastSpoken[num] = index + 1
        turn += 1
    nextNumber = 0
    while turn < turnNumber:
        nextNumberPrev = lastSpoken.get(nextNumber, None)
        lastSpoken[nextNumber] = turn
        # Number hasn't been spoken already.
        if nextNumberPrev == None:
            nextNumber = 0
        else:
            nextNumber = turn - nextNumberPrev
        turn += 1
    return nextNumber

def solvePart1():
    return str(playGameUpTo(2020))

def solvePart2():
    return str(playGameUpTo(30000000))

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())