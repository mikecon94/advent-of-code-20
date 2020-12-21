f = open("input", "r")
f = f.read()

inputRules = f.split("\n\n")[0].split("\n")
inputMessages = f.split("\n\n")[1].split("\n")

class rule:
    def __init__(self, ruleAsString):
        self.id = int(ruleAsString.split(":")[0])
        if "\"" in ruleAsString:
            self.rules = ruleAsString.split("\"")[1]
        else:
            self.rules = []
            self.currentList = []
            for token in ruleAsString.split(" "):
                if token.isdigit():
                    self.currentList.append(int(token))
                elif token == "|":
                    self.rules.append(self.currentList)
                    self.currentList = []
            self.rules.append(self.currentList)
    
    def evaluateRule(self, message, index, rules):
        # print(message, index)
        if isinstance(self.rules, str):
            if message[index] == self.rules:
                return True, index + 1
            else:
                return False, index
        else:
            # Loop round each set of rules checking if any match.
            for ruleSet in self.rules:
                ruleSetResult = False
                newIndex = index
                for id in ruleSet:
                    ruleSetResult, newIndex = rules[id].evaluateRule(message, newIndex, rules)
                    if not ruleSetResult:
                        newIndex = index
                        break
                if ruleSetResult:
                    return True, newIndex
        return False, index
                
def solvePart1():
    rules = dict()
    for ruleString in inputRules:
        newRule = rule(ruleString)
        rules[newRule.id] = newRule
        # print(newRule.id, newRule.rules)
    
    validMessages = 0
    for message in inputMessages:
        result = rules[0].evaluateRule(message, 0, rules)
        if result[0] and len(message) == result[1]:
            validMessages += 1
    
    return str(validMessages)

def solvePart2():
    return "2"

print("Part 1: " + solvePart1())
print("Part 2: " + solvePart2())