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
                # print("BUS ID: " + str(busId) + " DEPARTURE TIME: " + str(departureTime))
                if departureTime % int(busId) == 0:
                    earliestBusId = busId
                    busFound = True
                    break

    waitTime = departureTime - earliestDepartureTime
    # print("Departure Time: " + str(departureTime) + " Earliest: " + str(earliestDepartureTime))
    # print("EARLIEST: " + str(waitTime))
    return str(waitTime * int(earliestBusId))

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())