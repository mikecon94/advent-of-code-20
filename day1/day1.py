f = open("input", "r")
inputNums = []
for line in f.readlines():
    inputNums.append(int(line))

for num1 in range(len(inputNums)):
    for num2 in range(len(inputNums)):
        if inputNums[num1] + inputNums[num2] == 2020:
            result1 = inputNums[num1] * inputNums[num2]
        for num3 in range(len(inputNums)):
            if inputNums[num1] + inputNums[num2] + inputNums[num3] == 2020:
                result2 = inputNums[num1] * inputNums[num2] * inputNums[num3]

print("PART 1: " + str(result1))
print("PART 2: " + str(result2))
