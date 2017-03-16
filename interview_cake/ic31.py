def permutationsOfString(word):
    if len(word) < 2:
        return set(word)

    permutations = set()
    for ix in range(len(word)):
        wordToAdd = word[ix]

        if ix == len(word)-1:
            perms = permutationsOfString(word[:ix])
        elif ix > 0:
            perms = permutationsOfString(word[0:ix]+word[ix+1:])
        else:
            perms = permutationsOfString(word[1:])

        for item in perms:
            permutations.add(wordToAdd+item)

    return permutations


print(sorted(permutationsOfString("kat")))
