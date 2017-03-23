import random

def singlyRiffled(shuffled_deck, half1, half2):

    half1 = shuffled_deck[0]
    half2 = 0

    for i in range(1, len(shuffled_deck)):
        if shuffled_deck[i] == half1 + 1:
            half1 += 1
        elif shuffled_deck[i] == half2 + 1:
            half2 += 1
        else:
            return False

    return True

def singlyRiffled2(shuffled_deck, half1, half2):

    half1Ix = 0
    half2Ix = 0

    for i in range(0, len(shuffled_deck)):
        if half1Ix < len(half1) and shuffled_deck[i] == half1[half1Ix]:
            half1Ix += 1
        elif half2Ix < len(half2) and shuffled_deck[i] == half2[half2Ix]:
            half2Ix += 1
        else:
            return False

    return True

def riffle(deck):
    mid = random.randint(0, len(deck)-1)

    half1 = deck[:mid]
    half2 = deck[mid:]

    newDeck = list()

    while not (len(half1) == 0 and len(half2) == 0):
        if len(half1) > 0:
            topCards = random.randint(1, len(half1))
            newDeck.append(half1[:topCards])
            half1 = half1[topCards:]

        if len(half2) > 0:
            topCards = random.randint(1, len(half2))
            newDeck.append(half2[:topCards])
            half2 = half2[topCards:]

    return newDeck

deck = list(range(1, 52+1))
random.shuffle(deck)
print(deck)
print(singlyRiffled2(deck, deck[:34], deck[34:]))
