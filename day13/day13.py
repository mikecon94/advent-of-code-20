f = open("input", "r")
f = f.read()
lines = f.split("\n")
earliestDepartureTime = int(lines[0])
busIds = []
for busId in lines[1].split(","):
    busIds.append(busId)

def solvePart1():
    departureTime = earliestDepartureTime
    earliestBusId = 0
    busFound = False
    while not busFound:
        departureTime += 1
        for busId in busIds:
            if busId != "x":
                if departureTime % int(busId) == 0:
                    earliestBusId = busId
                    busFound = True
                    break

    waitTime = departureTime - earliestDepartureTime
    return str(waitTime * int(earliestBusId))

def findMax():
    highestId = 0
    highestIndex = 0
    for index, busId in enumerate(busIds):
        if busId != "x":
            if int(busId) > highestId:
                highestId = int(busId)
                highestIndex = index
    return highestIndex, highestId

def findPossibleDepartureTime(greatestBusId, startingValue):
    timeFound = False
    time = startingValue
    while not timeFound:
        time += 1
        if time % greatestBusId == 0:
            return time

def product():
    product = 1
    for x in busIds:
        if x != "x":
            product *= int(x)
    return product

def gcd(a, b):
    if b > a:
        tempA = a
        a = b
        b = tempA
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        # Find Remainder
        # A = B*Q + R
        # gcd(B, R)
        return gcd(b, a % b)

#This one hurts my head
def solvePart2():
    # Start with highest Number and find multiples from there.
    greatestIndex, greatestBusId = findMax()

    countOfMatches = 0
    # checkDepartureTime = findPossibleDepartureTime(greatestBusId, 0)
    
    # https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
    # https://rosettacode.org/wiki/Chinese_remainder_theorem
    # https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
    # https://www.reddit.com/r/adventofcode/comments/kcb3bb/2020_day_13_part_2_can_anyone_tell_my_why_this/
    # https://www.geeksforgeeks.org/chinese-remainder-theorem-set-2-implementation/
    totalProduct = product()
    timestamp = int(busIds[0])
    for index, id in enumerate(busIds):
        if id != "x":
            id = int(id)
            pp = totalProduct // id
            timestamp += (index+1) * gcd(pp, id) * pp
    return str(timestamp % totalProduct)


    # for index, id in enumerate(busIds):
    #     if id != "x":
    #         id = int(id)
    #         timestamp += -index * (totalProduct // id) * pow(totalProduct // id, -1, id)
    # return str(timestamp % totalProduct)
    checkDepartureTime = findPossibleDepartureTime(int(greatestBusId), 1202160085)
    bDict = dict()
    for id in busIds:
        if id != "x":
            id = int(id)
            bi = totalProduct // id
            biDash = gcd(bi, id)
            bDict[id] = {'bi': bi, 'biDash': biDash}
    
    sum = -1
    while sum % totalProduct != 0:
        sum = 0
        for index, id in enumerate(busIds):
            if id != "x":
                id = float(id)
                bi = float(bDict.get(id).get('bi'))
                biDash = float(bDict.get(id).get('biDash'))
                # bi = totalProduct/id
                # biDash = (1/bi) % id # This is wrong.
                # We need GCD of bi & id
                # biDash = gcd(bi, id)
                # ai = 1068781 + index
                ai = float(checkDepartureTime - (greatestIndex - index))
                # ai = float(checkDepartureTime + index)
                sum += float(bi * biDash * ai)
        checkDepartureTime += greatestBusId
        # checkDepartureTime += int(busIds[0])
        # print(str(sum%totalProduct))
        assert(checkDepartureTime < totalProduct)
    return str(checkDepartureTime - greatestBusId - greatestIndex)
    # First Attempt - Brute Force Solution that was too slow:
    # while countOfMatches < len(busIds):
    #     checkDepartureTime += greatestBusId
    #     countOfMatches = 0
    #     for index, busId in enumerate(busIds):
    #         # print("BUS ID: " + str(busId))
    #         if busId == "x":
    #             countOfMatches += 1
    #         elif int(busId) == greatestBusId:
    #             countOfMatches += 1
    #         else:
    #             # print("CHECKING: " + str(checkDepartureTime - (greatestIndex - index)))
    #             if (checkDepartureTime - (greatestIndex - index)) % int(busId) == 0:
    #                 countOfMatches += 1
    #             else:
    #                 break
    return str(checkDepartureTime - greatestIndex)

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())