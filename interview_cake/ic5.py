def cashWays(amount, denominations):

    combinations = [[] for y in range(amount+1)]

    for i in range(amount+1):
        if i == 0:
            combinations[i] = [[]]

        else:
            for den in denominations:
                if den <= i:
                    for comb in combinations[i-den]:
                        if not comb or (comb and comb[len(comb)-1] >= den):
                            combinations[i].append(comb+[den])

    return combinations[amount]


print(cashWays(5, [1, 5, 3]))




#should return:
# 1¢, 1¢, 1¢, 1¢
# 1¢, 1¢, 2¢
# 1¢, 3¢
# 2¢, 2¢
