class Field:
    def __init__(self, name, validValues):
        self.name = name
        self.validValues = validValues
    
    def print(self):
        print("FIELD: " + self.name + " VALID VALUES: " + str(self.validValues))

fields = dict()

#Capture all valid values in a set

setOfTotalValidValues = set()
f = open("input", "r")
f = f.read()
input = f.split("\n\n")
ticketFields = input[0]
for field in ticketFields.split("\n"):
    fieldName = field.split(": ")[0]
    # Could be changed to a Set in case of overlap.
    validValues = set()
    valueRanges = field.split(": ")[1].split(" or ")
    for vRange in valueRanges:
        min = int(vRange.split("-")[0])
        max = int(vRange.split("-")[1])
        values = list(range(min, max+1))
        setOfTotalValidValues.update(values)
        validValues.update(values)
    fields[fieldName] = Field(fieldName, validValues)

# for field in fields:
#     fields[field].print()

def parseTicket(ticket):
    returnTicket = []
    for value in ticket.split(","):
        returnTicket.append(int(value))
    return returnTicket

ticket = input[1].split("\n")[1]
myTicket = parseTicket(ticket)

nearbyTickets = []
nearbyTicketsInput = input[2]
nearbyTicketsInput = nearbyTicketsInput.split("\n")
nearbyTicketsInput.pop(0)
for ticket in nearbyTicketsInput:
    nearbyTickets.append(parseTicket(ticket))

# Check all nearby tickets for any values that aren't valid in any of fields.
# Return list of valid tickets & sum of invalid values 
def getValidTickets(tickets):
    validTickets = []
    invalidValuesSum = 0
    for ticket in nearbyTickets:
        validTicket = True
        for value in ticket:
            if value not in setOfTotalValidValues:
                validTicket = False
                invalidValuesSum += value
                break
        if validTicket:
            validTickets.append(ticket)
    return validTickets, invalidValuesSum

# Input is:
# fields - Array of Field objects containing name and valid values.
# myTicket - Array of field values for my ticket.
# nearbyTickets - Array of tickets (tickets represented as an array of field values)
def solvePart1():
    return str(getValidTickets(nearbyTickets)[1])

def myFunc(e):
    return len(e)

def solvePart2():
    # Discard tickets that aren't valid
    validNearbyTickets = getValidTickets(nearbyTickets)[0]
    validNearbyTickets.append(myTicket)

    # Populate a Set for each index that will be the starting point.
    # The Set will contain all field names.
    fieldPosition = []
    for index in range(0, len(myTicket)):
        fieldSet = set()
        for field in fields:
            fieldSet.add(field)
        fieldPosition.append(fieldSet)
    # We will then iterate over each value in each ticket and check whether the value is valid for that field.
    # If not we remove that field name from the set of options for that index.
    # Repeat until we have a single field for all indexes.
    for ticket in validNearbyTickets:
        # print(ticket)
        for index, value in enumerate(ticket):
            # print(index, fieldPosition[index], value)
            newFieldSet = fieldPosition[index].copy()
            for fieldName in fieldPosition[index]:
                # print("FIELD: " + fieldName + " VALID: " + str(fields.get(fieldName).validValues))
                if value not in fields.get(fieldName).validValues:
                    # print("REMOVING FIELD: " + fieldName)
                    newFieldSet.remove(fieldName)
                    # print(newFieldSet)
            fieldPosition[index] = newFieldSet

    fieldPositionsByCount = dict()
    for field in fieldPosition:
        fieldPositionsByCount[len(field)] = field

    newFieldPositions = dict()
    for index, field in enumerate(fieldPosition):
        if len(field) != 1:
            field = field.difference(fieldPositionsByCount[len(field)-1])
        newFieldPositions[index] = field.pop()

    result = 1
    for field in newFieldPositions:
        if "departure" in newFieldPositions[field]:
            result *= myTicket[field]

    return str(result)
    # sortedFieldPositions = list(fieldPosition)
    # sortedFieldPositions.sort(key=myFunc, reverse = True)
    # print(sortedFieldPositions)
    # print(sortedFieldPositions[1].difference(sortedFieldPositions[2]))
    # [print(len(field)) for field in sortedFieldPositions ]

    # Optimizations -
    #   Done - Change Field valid values to a Set to quickly check if a value is valid.
    #   Done - Change list of fields into a Map(Field Name, values) - we can then just loop over the Set of valid names for an index
    #          and quickly access those Fields from the Map instead of searching a list.

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())
