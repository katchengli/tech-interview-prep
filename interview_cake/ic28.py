def findPosClosingParenthesis(phrase, openingParPos):
    opParenthesisCount = 0

    for i in range(openingParPos+1, len(phrase)):
        if phrase[i] == '(':
            opParenthesisCount += 1
        elif phrase[i] == ')':
            if opParenthesisCount == 0:
                return i
            opParenthesisCount -= 1

    return None # or raise error..

phrase = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print(findPosClosingParenthesis(phrase, 10))
# should return 79
