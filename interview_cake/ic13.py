#Comments: Below is the algorithm I had come up with forgetting that strings cannot
#be compared like numbers....
#In IC's answer, they compare the word at the middle index with each of the extremities
#instead of doing the opposite... Which is smarter. They also don't consider an unrotated list.
# In that case, we need to identify that the first item of the part of the list
#considered is always alphabetically after the right side of the guess index

def findRotatingPoint(words):
    minIx = 0
    maxIx = len(words) - 1
    diff = abs(words[maxIx] - words[minIx])
    while True:
        midIx = (maxIx - minIx) // 2
        compareList = [(words[minIx], 0), (words[midIx], 1), (words[maxIx], 2)]
        compareList.sort()
        tempDiff1 = abs(words[maxIx] - word[midIx])#does not work lol
        tempDiff2 = abs(words[minIx] - word[midIx])

        if tempDiff1 > tempDiff2:
            if tempDiff1 > diff:
                minIx = midIx
            else:
                return getFirstWordIx(minIx, maxIx, len(words))
        elif tempDiff2 > tempDiff1:
            if tempDiff2 > diff:
                maxIx = midIx
            else:
                return getFirstWordIx(minIx, maxIx)

#Interview Cake answer with added trace:
def find_rotation_point(words):

    first_word = words[0]

    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
        # guess a point halfway between floor and ceiling
        guess_index = floor_index + ((ceiling_index - floor_index) // 2)
        print('fix: ' + str(floor_index) + ' ' + words[floor_index] + ', gix: ' + str(guess_index) + ' ' + words[guess_index] + ', cix: ' + str(ceiling_index)+ ' ' + words[ceiling_index])

        # if guess comes after first word or is the first word
        if words[guess_index] >= first_word:
            # go right
            floor_index = guess_index
        else:
            # go left
            ceiling_index = guess_index

        # if floor and ceiling have converged
        if floor_index + 1 == ceiling_index:

            # between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return ceiling_index

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

words2 = [
    'f',
    'g',
    'h',
    'a',
    'b',
    'c',
    'd',
    'e',
]

#print(words[findRotatingPoint(words)])
print(words[find_rotation_point(words)])
print(words2[find_rotation_point(words2)])
