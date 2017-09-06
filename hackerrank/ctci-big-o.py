from math import sqrt, ceil

def isPrime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2, int(ceil(sqrt(number)))+1):
        if number%i == 0:
            return False

    return True

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if isPrime(n) == True:
        print("Prime")
    else:
        print("Not prime")
