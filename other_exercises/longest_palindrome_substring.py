def isPalindrome(word):
    for i in range(len(word)/2):
        if word[i] != word[-i-1]:
            return False

    return True

def findAllPalindromes(word):
    palindromes = dict()
    longestRepeatingPalindrome = ''
    for i in range(len(word)):
        for j in range(i, len(word)):
            if isPalindrome(word[i:j+1]):
                if word[i:j+1] in palindromes:
                    if len(longestRepeatingPalindrome) < len(word[i:j+1]):
                        longestRepeatingPalindrome = word[i:j+1]
                    palindromes[word[i:j+1]] += 1
                else:
                    palindromes[word[i:j+1]] = 1
    print(palindromes)
    return longestRepeatingPalindrome

print(findAllPalindromes('banana'))
print(findAllPalindromes('bananab' * 2))
