class shunting_yard:
    def __init__(self, expression):
        self.rpn = self.parseExpression(expression)

    def evaluate(self):
        stack = []
        for token in self.rpn:
            if isinstance(token, int):
                stack.append(token)
            elif token == "+":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand1 + operand2)
            elif token == "*":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand1 * operand2)
        return stack.pop()

    def parseExpression(self, expression):
        operatorStack = []
        outputQueue = []
        for char in expression:
            if char == " ":
                pass
            else:
                if char.isdigit():
                    outputQueue.append(int(char))
                elif char in ["*", "+"]:
                    if char == "*":
                        while operatorStack != [] and operatorStack[-1] == "+":
                            outputQueue.append(operatorStack.pop())
                    operatorStack.append(char)
                elif char == "(":
                    operatorStack.append(char)
                elif char == ")":
                    operator = operatorStack.pop()
                    while operator != "(":
                        outputQueue.append(operator)
                        operator = operatorStack.pop()
        while operatorStack != []:
            operator = operatorStack.pop()
            outputQueue.append(operator)
        return outputQueue