f = open("input", "r")
f = f.read()
lines = f.split("\n")

class expression:

    def __init__(self, type, value, lExpression, rExpression):
        self.lExpression = 0
        self.rExpression = 0
        self.type = "leaf"
        self.value = 0
        self.__parse(expression)

    def evaluate(self):
        if self.type == "leaf":
            return self.value
        else:
            lhs = lExpression.evaluate()
            rhs = rExpression.evaluate()
            if self.type == "*":
                return lhs * rhs
            elif self.type == "+":
                return lhs + rhs
            else:
                raise ArithmeticError("Unknown Operator")

def parseExpression(strExpression):
    tokens = strExpression.split(" ")
    print(tokens)
    pass


class leafNode:
    def __init__(self, value):
        self.value = value

def evaluate(expression):
    print("EVALUATING:", expression)
    sum = 0
    stack = 0
    subExpression = False
    subExpressionStr = ""
    currentOp = "nop"
    for token in expression.split(" "):
        if subExpression:
            subExpressionStr += " " + token.replace(")", "")
            if token.endswith(")"):
                if stack == 1:
                    subExpression = False
                    if currentOp == "nop":
                        sum = evaluate(subExpressionStr)
                    elif currentOp == "*":
                        sum *= evaluate(subExpressionStr)
                    elif currentOp == "+":
                        sum += evaluate(subExpressionStr)
                    subExpressionStr = ""
                else:
                    stack -= 1
        else:
            if token.isdigit():
                if currentOp == "nop":
                    sum = int(token)
                elif currentOp == "*":
                    sum *= int(token)
                elif currentOp == "+":
                    sum += int(token)
            elif token in ["+", "*"]:
                currentOp = token
        if token.startswith("("):
            stack += 1
            token = token.replace("(", "")
            subExpressionStr += token
            subExpression = True
    return sum

def solvePart1():
    # print("RESULT:", expression("1 + 2 * 3 + 4 * 5 + 6").evaluate())
    # Loop over each expression
    # sum = 0
    # for line in lines:
    #     currentExpression = expression(line)
    #     sum += currentExpression.evaluate()
    #     print(line)
    print(evaluate("1 + 2 * 3 + 4 * 5 + 6"))
    expression = "1 + (2 * 3) + 4 * (5 + 6)"
    return str(evaluate(expression))

    return str(0)

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())