def checkParentesisMatching(phrase):
    openersStack = list()

    for bracket in phrase:
        if bracket == '(' or  bracket == '[' or  bracket == '{':
            openersStack.append(bracket)
        elif bracket == ')':
            if not openersStack or openersStack.pop() != '(':
                return False
        elif bracket == ']':
            if not openersStack or openersStack.pop() != '[':
                return False
        elif bracket == '}':
            if not openersStack or openersStack.pop() != '{':
                return False

    if openersStack:
        return False

    return True

print(checkParentesisMatching("{[]()}"))#True
print(checkParentesisMatching("{[(])}"))#False
print(checkParentesisMatching("{[}"))#False
print(checkParentesisMatching("(("))#False
print(checkParentesisMatching("))"))#False
print(checkParentesisMatching(""))#True
