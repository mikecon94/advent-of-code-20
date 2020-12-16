class Field:
    def __init__(self, name, validValues):
        self.name = name
        self.validValues = validValues
    
    def print(self):
        print("FIELD: " + self.name + " VALID VALUES: " + str(self.validValues))

fields = []
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

def solvePart1():
    # Input is:
    # fields - Array of Field objects containing name and valid values.
    # myTicket - Array of field values for my ticket.
    # nearbyTickets - Array of tickets (tickets represented as an array of field values)
    return "1"

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())
