f = open("input", "r")

columns = 0
rows = 0

map = []
for line in f.readlines():
    row = []
    for char in line:
        if(char != "\n"):
            row.append(char)
    map.append(row)
rows = len(map)
columns = len(map[0])

noOfTrees = 0
tobogganColumn = 0
tobogganRow = 0

while tobogganRow < rows:
    if map[tobogganRow][tobogganColumn] == "#":
        noOfTrees += 1
    tobogganRow += 1
    
    tobogganColumn += 3
    if tobogganColumn >= columns:
        tobogganColumn = tobogganColumn - columns

print(noOfTrees)