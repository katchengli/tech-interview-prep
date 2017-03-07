import sys

#note: we don't need a matrix because we simply need to keep track of the max value at each level instead. Easy to modify
def max_duffel_bag_value(cake_tuples, capacity):
    calMatrix = [[0 for _ in range(len(cake_tuples))] for _ in range(capacity+1)] # we want the max value in each cell...
    max_int = sys.maxsize

    for i in range(capacity+1):
        for j in range(len(cake_tuples)):
            if cake_tuples[j][0] == 0 and cake_tuples[j][1] > 0:
                return max_int

            if cake_tuples[j][0] == 0 and cake_tuples[j][1] == 0 or cake_tuples[j][0] > i:
                calMatrix[i][j] = 0
            else:
                weight = cake_tuples[j][0]
                nb = i//weight
                thisTotal = nb*cake_tuples[j][1]
                thisWeight = nb*weight
                calMatrix[i][j] =  thisTotal + max(calMatrix[i-thisWeight])

    return max(calMatrix[capacity])

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20
print(max_duffel_bag_value(cake_tuples, capacity))
#returns 555
cake_tuples = [(0, 160), (3, 90), (2, 15)]
capacity = 20
print(max_duffel_bag_value(cake_tuples, capacity))
#returns max_int
cake_tuples =   [(1, 30), (50, 200)]
capacity = 100
print(max_duffel_bag_value(cake_tuples, capacity))
#returns 3000
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 0
print(max_duffel_bag_value(cake_tuples, capacity))
#returns 0
cake_tuples = [(0, 0), (3, 90), (2, 15)]
capacity = 1
print(max_duffel_bag_value(cake_tuples, capacity))
#returns 0
