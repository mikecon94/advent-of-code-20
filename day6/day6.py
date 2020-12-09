f = open("input", "r")

inputs = f.read()
inputs = inputs.split("\n\n")

groups = []
for group in inputs:
    groups.append(group.split("\n"))


def solvePart1():
    sumOfQuestionsAnswered = 0
    for group in groups:
        questionSet = set()
        for answer in group:
            for char in answer:
                questionSet.add(char)
        sumOfQuestionsAnswered += len(questionSet)
    return str(sumOfQuestionsAnswered)

def solvePart2():
    questionsAnswered = 0
    for group in groups:
        questionDict = dict()
        numberOfPeople = len(group)
        for person in group:
            for answer in person:
                questionDict[answer] = (questionDict.get(answer, 0) + 1)
        for question in questionDict:
            if questionDict.get(question) == numberOfPeople:
                questionsAnswered += 1
    return str(questionsAnswered)

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())