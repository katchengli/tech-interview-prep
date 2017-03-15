def permutationIsPalindrome(word):
    alphabet = [0]*26

    for letter in word:
        alphabet[translateLetterInIx(letter)] = ~alphabet[translateLetterInIx(letter)]

    if sum(alphabet) < -1:
        return False
    else:
        return True

def translateLetterInIx(letter):
    return ord(letter) - 97

print(permutationIsPalindrome("civic"))#True
print(permutationIsPalindrome("ivicc"))#True
print(permutationIsPalindrome("civil"))#False
print(permutationIsPalindrome("livci"))#False

#IC approach
def permutationIsPalindrome2(word):
    characters = set()

    for letter in word:
        if letter in characters:
            characters.remove(letter)
        else:
            characters.add(letter)

    if len(characters) > 1:
        return False

    return True
print(permutationIsPalindrome2("civic"))#True
print(permutationIsPalindrome2("ivicc"))#True
print(permutationIsPalindrome2("civil"))#False
print(permutationIsPalindrome2("livci"))#False
