def wordCloud(phrase):
    print(phrase)
    phrase = phrase.lower()
    phrase = phrase.replace(",", " ")
    phrase = phrase.replace(".", " ")
    phrase = phrase.replace(":", "")
    phrase = phrase.replace(";", "")
    print(phrase)
    phrase = phrase.replace("'", " ")
    print(phrase)
    phrase = phrase.replace('"', "")
    phrase = phrase.replace(')', "")
    phrase = phrase.replace('(', "")

    print(phrase)
    phraseList = phrase.split()
    wordCloud = dict()

    for word in phraseList:
        if word in wordCloud:
            wordCloud[word] += 1
        else:
            wordCloud[word] = 1

    return wordCloud


#phrase = 'After beating the eggs, Dana read the next step: Add "milk" and eggs, then add flour and sugar.'
#print(wordCloud(phrase))
phrase = 'We came, we saw, we conquered...then we ate Bill\'s (Mille-Feuille) cake. The bill came to five dollars.'
#print(wordCloud(phrase))

def wordCloud2(phrase):
    wordCloud = dict()
    phrase = phrase.replace('"', "")
    phrase = phrase.replace(')', "")
    phrase = phrase.replace('(', "")
    phrase = phrase.replace(": ", " :")
    phrase = phrase.replace(";", "")
    phrase = phrase.replace(',', "")
    phrase = phrase.replace("...", ". ")
    phrase = phrase.replace(". ", " .")
    phrase = phrase.replace("'", " '")
    phraseList = phrase.split()

    if len(phraseList) < 1:
        return dict()

    phraseList[0] = phraseList[0].lower()
    for word in phraseList:
        if word[0] == ".":
            word = word[1:].lower()
        elif word[0] == ":":
            word = word[1:].lower()

        if word[len(word)-1] == ".":
            word = word[:len(word)-1]

        if word in wordCloud:
            wordCloud[word] += 1
        else:
            wordCloud[word] = 1

    return wordCloud

def wordCloud3(phrase):
    wordCloud = dict()
    phraseList = wordCloudSplit(phrase)

    for word in phraseList:
        if word in wordCloud:
            wordCloud[word] += 1
        else:
            wordCloud[word] = 1

    return wordCloud

# character is a variable holding a string with length 1
def is_letter(character):
    return character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'

def wordCloudSplit(phrase):
    if len(phrase) == 0:
        return []
    listOfWords = list()
    listOfCharacters = list(phrase)
    listOfCharacters[0] = listOfCharacters[0].lower()
    wordList = list()
    prevChar = None
    prevPrevChar = None
    for character in listOfCharacters:
        if is_letter(character):
            if prevPrevChar and prevPrevChar in '.!?:':
                character = character.lower()
            wordList.append(character)
        else:
            if len(wordList) != 0:
                listOfWords.append(''.join(wordList))
                wordList = list()

        prevPrevChar = prevChar
        prevChar = character

    return listOfWords

#phrase = 'After beating the eggs, Dana read the next step: Add "milk" and eggs, then add flour and sugar.'
print(wordCloud3(phrase))
