def enumerateCombinations(optionsSets):
    results = list()
    results.append([])

    for i in optionsSets:
        newResults = list()
        for x in i:
            for k in results:
                newResults.append(k+list(x))

        results = newResults
    return results

optionSet = [['a','b'], ['c','d']]

print(enumerateCombinations(optionSet))
