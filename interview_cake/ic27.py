def reverse_words(message):
    msgList = list(message)
    listLen = len(msgList)
    wordLastLen = 0
    wordStack = list()
    wordStack.append(' ')
    forwardIx = 0
    for _ in range(len(msgList)-1, -1, -1):
        if (msgList[-wordLastLen-1] == ' '):
            wordLastLen += 1

            for i in range(listLen-wordLastLen-1, forwardIx-1, -1):
                msgList[i+wordLastLen] = msgList[i]

            for j in range(forwardIx, forwardIx+wordLastLen):
                msgList[j] = wordStack.pop()

            forwardIx += wordLastLen
            wordLastLen = 0
            wordStack.append(' ')
        else:
            wordLastLen += 1
            wordStack.append(msgList[-wordLastLen])

    return ''.join(msgList)

#solution: we need to reverse the whole message first and then reverse each word separately
def reverse_words2(message):
    msgList = list(message)
    reverseList(msgList)

    wordBeginning = 0
    for i in range(len(msgList)):
        if msgList[i] == ' ':
            msgList[wordBeginning:i] = reverseList(msgList[wordBeginning:i])
            wordBeginning = i+1
        elif i == len(msgList)-1:
            msgList[wordBeginning:] = reverseList(msgList[wordBeginning:i+1])

    return ''.join(msgList)

def reverseList(wordList):
    for i in range(len(wordList)//2):
        wordList[i], wordList[-i-1] = wordList[-i-1], wordList[i]

    return wordList

message = 'find you will pain only go you recordings security the into if'

print(reverse_words2(message))
# returns: 'if into the security recordings you go only pain will you find'
