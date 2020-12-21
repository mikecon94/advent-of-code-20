f = open("input", "r")
f = f.read()
lines = f.split("\n")

def countTokensInString(string, token):
    total = 0
    for char in string:
        if char == token:
            total += 1
    return total

def evaluate(expression):
    sum = 0
    currentOp = "nop"
    stack = 0
    subExpression = ""
    for token in expression.split(" "):
        if stack >= 1:
            if token.endswith(")"):
                stack -= countTokensInString(token, ")")
                if stack < 1:
                    subExpression += token[:-1] + " "
                else:
                    subExpression += token + " "
                if stack == 0:
                    if currentOp == "+":
                        sum += evaluate(subExpression)
                    elif currentOp == "*":
                        sum *= evaluate(subExpression)
                    elif currentOp == "nop":
                        sum = evaluate(subExpression)
                    subExpression = ""
            elif token.startswith("("):
                stack += countTokensInString(token, "(")
                subExpression += token + " "
            else:
                subExpression += token + " "
        else:
            if token.startswith("("):
                stack += countTokensInString(token, "(")
                subExpression += token[1:] + " "
            elif token.isdigit():
                if currentOp == "nop":
                    sum = int(token)
                elif currentOp == "+":
                    sum += int(token)
                elif currentOp == "*":
                    sum *= int(token)
            elif token in ["*", "+"]:
                currentOp = token
    return sum

def solvePart1():
    sum = 0
    for line in lines:
        sum += evaluate(line)
    return str(sum)

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())