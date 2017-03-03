#Trie implementation time!
#Not really my own implementation as it is heavily based on the problem's answer.. The answer was a Trie plain and simple

class URLTrie(object):
    def __init__(self):
        self.root = {}

    def insert_word(self, word):
        newWord = False
        currentNode = self.root

        for char in word:
            if char not in currentNode:
                currentNode[char] = {}
                currentNode = currentNode[char]
                newWord = True

        if "wordEnd" not in currentNode:
            newWord = True
            currentNode["wordEnd"] = {}


    return newWord
