from passport import Passport

f = open("input", "r")

inputs = f.read()
inputs = inputs.split("\n\n")

passports = []
for record in inputs:
    passport = Passport()
    recordLines = record.split("\n")
    for line in recordLines:
        fields = line.split(" ")
        if line == '':
            break
        for keyValue in fields:
            key = keyValue.split(":")[0]
            value = keyValue.split(":")[1]
            passport.setProperty(key, value)
    passports.append(passport)

def solvePart1():
    validPassportsCount = 0
    for passport in passports:
        if passport.isValid():
            validPassportsCount += 1
    return str(validPassportsCount)

def solvePart2():
    validPassportsCount = 0
    for passport in passports:
        if passport.isValid():
            if passport.isSchemaValid():
                validPassportsCount += 1
    return str(validPassportsCount)

print("Part 1: " + solvePart1())

#135 is too low
#185 is too high
print("Part 2: " + solvePart2())