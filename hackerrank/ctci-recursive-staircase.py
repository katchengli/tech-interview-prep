totalsMap = {0:0, 1:1, 2:2, 3:4}
def climb(n):
    total = 0
    if n in totalsMap:
        return totalsMap[n]

    for i in range(1, 4):
        leftoverTotal = n-i
        if leftoverTotal >= 0:
            if leftoverTotal in totalsMap:
                total += totalsMap[leftoverTotal]
            else:
                newOptions = climb(leftoverTotal)
                totalsMap[leftoverTotal] = newOptions
                total += newOptions
    return total

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(climb(n))
