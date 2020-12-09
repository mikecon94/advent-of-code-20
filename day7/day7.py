class Bag:
    colour = ""
    def __init__(self, bagColour):
        self.colour = bagColour
        #"white bag": 2 - 2 white bags allowed in this Bag
        self.childBags = dict()

    def addChildBag(self, colour, numberAllowed):
        self.childBags[colour] = numberAllowed

f = open("input", "r")
rules = f.read()
rules = rules.split("\n")
allBags = []

for rule in rules:
    currentBag = Bag(rule.split(" bags ")[0])
    ruleTokens = rule.split(" ")
    if ruleTokens[4] != "no":
        endOfLine = False
        index = 4
        while not endOfLine:
            childQuantity = ruleTokens[index]
            childColour = ruleTokens[index + 1] + " " + ruleTokens[index + 2]
            currentBag.addChildBag(childColour, childQuantity)
            if ruleTokens[index + 3].endswith("."):
                endOfLine = True
            else:
                index += 4
            allBags.append(currentBag)

def printAllBags():
    for bag in allBags:
        print("COLOUR: " + bag.colour + " CHILDREN: " + str(bag.childBags))

def solvePart1():
    setOfBags = set()
    for bag in allBags:
        if bag.colour == 'shiny gold':
            setOfBags.add(bag)
    change = True
    while change:
        change = False
        for bag in allBags:
            if not setOfBags.__contains__(bag):
                for containingBag in setOfBags:
                    if bag.childBags.get(containingBag.colour) != None:
                        change = True
                        setOfBags.add(bag)
                        break
    return str(len(setOfBags) - 1)

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())