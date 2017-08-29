# t is the number of trips to the ice cream parlor
# 3t subsequent entries
# for each t, first line contains money m, second line contains the number of flavors n,
# and the third line contains n space-separated integers indicating the cost of each
# flavor cost(i) where i E 1 <= i <= n

def returnIceCreams(m, n, a):
    costMap = {}
    for i in range(n):
        if a[i] in costMap:
            costMap[a[i]].append(i+1)
        else:
            costMap[a[i]] = [i+1]

    for k, v in costMap.items():
        j = m-k
        first = v[0]
        second = 0
        if j in costMap:
            if k != j:
                second = costMap[j][0]
            elif len(v) > 1:
                second = v[1]

            if first > second:
                return str(second) + ' ' + str(first)
            else:
                return str(first) + ' ' + str(second)

###
t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print(returnIceCreams(m, n, a))
