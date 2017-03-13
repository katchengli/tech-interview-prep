def mockReverseString(word):
    wordList = list(word)
    wordList2 = list(word) #suggestion de Mathieu :)

    lastIx = len(wordList) - 1
    for i in range(len(wordList)//2):
        wordList[i], wordList[lastIx] = wordList[lastIx], wordList[i]
        wordList2[i], wordList2[-i-1] = wordList2[-i-1], wordList2[i]
        lastIx -= 1

    return ''.join(wordList)


word = "finalement"
print(mockReverseString(word))
#should return 'tnemelanif'
