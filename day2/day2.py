f = open("input", "r")

p1Violations = 0
p2Violations = 0
count = 0
p2Valid = 0
for line in f.readlines():
    count += 1
    parts = line.split(":")
    policy = parts[0]
    password = parts[1]
    password = password.strip()
    policyParts = policy.split(" ")
    policyLetter = policyParts[1]
    min = policyParts[0].split("-")[0]
    max = policyParts[0].split("-")[1]
    
    letterCount = 0
    charIndex = 0
    p2Met = 0
    for char in password:
        if charIndex == int(min)-1 or charIndex == int(max)-1:
            if char == policyLetter:
                p2Met += 1
        if char != "\n":
            if char == policyLetter:
                letterCount += 1
                if letterCount > int(max):
                    p1Violations += 1
                    break
        charIndex += 1
    if p2Met == 1:
        p2Valid += 1
    if letterCount < int(min):
        p1Violations += 1

print("Part 1: " + str(count - p1Violations))
print("Part 2: " + str(p2Valid))