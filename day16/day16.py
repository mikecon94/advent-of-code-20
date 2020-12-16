class Field:
    def __init__(self, name, validValues):
        self.name = name
        self.validValues = validValues
    
    def print(self):
        print("FIELD: " + self.name + " VALID VALUES: " + str(self.validValues))

fields = []
#Capture all valid values in a set

setOfTotalValidValues = set()
f = open("input", "r")
f = f.read()
input = f.split("\n\n")
ticketFields = input[0]
for field in ticketFields.split("\n"):
    fieldName = field.split(": ")[0]
    # Could be changed to a Set in case of overlap.
    validValues = []
    valueRanges = field.split(": ")[1].split(" or ")
    for vRange in valueRanges:
        min = int(vRange.split("-")[0])
        max = int(vRange.split("-")[1])
        values = list(range(min, max+1))
        setOfTotalValidValues.update(values)
        validValues += values
    fields.append(Field(fieldName, validValues))

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

# Input is:
# fields - Array of Field objects containing name and valid values.
# myTicket - Array of field values for my ticket.
# nearbyTickets - Array of tickets (tickets represented as an array of field values)

def solvePart1():
    # Check all nearby tickets for any values that aren't valid in any of fields.

    invalidNumbers = 0
    for ticket in nearbyTickets:
        for value in ticket:
            if not value in setOfTotalValidValues:
                invalidNumbers += value

    return str(invalidNumbers)

def solvePart2():
    # Discard tickets that aren't valid
    validNearbyTickets = []
    for ticket in nearbyTickets:
        validTicket = True
        for value in ticket:
            if value not in setOfTotalValidValues:
                validTicket = False
                break
        if validTicket:
            validNearbyTickets.append(ticket)

    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())
