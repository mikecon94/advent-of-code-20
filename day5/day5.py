f = open("input", "r")

inputs = f.read()
inputs = inputs.split("\n")

def binarySearch(minNumber, maxNumber, upperHalf, index):
    print(str(minNumber) + " " + str(maxNumber) + str(upperHalf) + str(index))
    if (maxNumber - minNumber) == 1:
        if upperHalf[index]:
            return maxNumber
        else:
            return minNumber
    else:
        difference = maxNumber - minNumber
        if difference % 2 != 0:
            difference += 1

        if upperHalf[index]:
            minNumber += int(difference) / 2
        else:
            maxNumber -= int(difference) / 2
        
        index += 1
        return binarySearch(int(minNumber), int(maxNumber), upperHalf, index)

seatIds = []
for boardingPass in inputs:
    print(boardingPass)
    upperHalf = []
    for i in range(0,7):
        if boardingPass[i] == 'F':
            upperHalf.append(False)
        else:
            upperHalf.append(True)
    rowNumber = binarySearch(0, 127, upperHalf, 0)
    upperHalf = []
    for j in range(7, 10):
        print(boardingPass[j])
        if boardingPass[j] == 'L':
            upperHalf.append(False)
        else:
            upperHalf.append(True)
    columnNumber = binarySearch(0, 7, upperHalf, 0)
    seatId = (rowNumber * 8) + columnNumber
    print(str(rowNumber) + " " + str(columnNumber))
    seatIds.append(seatId)
print(seatIds)

def solvePart1():
    maxSeatId = 0
    for seatId in seatIds:
        if seatId > maxSeatId:
            maxSeatId = seatId
    return str(maxSeatId)

def solvePart2():
    return str(2)

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())