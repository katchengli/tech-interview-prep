#constraint: do not use division in your solution
def get_products_of_all_ints_except_at_index(listOfInts):
    listOfProducts = [1]*len(listOfInts) #initialize list to neutral mult array

    for x in range(len(listOfInts)):
        for y in range(len(listOfInts)):
            if x != y:
                listOfProducts[x] *= listOfInts[y]

    return listOfProducts

testList = [1,7,3,4]
print(get_products_of_all_ints_except_at_index(testList))
#should return [84,12,28,21]

def get_products_of_all_ints_except_at_index2(listOfInts):
    if len(listOfInts) < 2:
        raise IndexError('Getting the product of numbers at other indices requires at least 2 numbers')

    listOfProducts = [1]*len(listOfInts) #initialize list

    # populating the list with the left of the index products
    leftIxProduct = 1
    for x in range(1, len(listOfInts)):
        leftIxProduct *= listOfInts[x-1]
        listOfProducts[x] = leftIxProduct

    # populating the list with the right of the index products
    rightIxProduct = 1
    for y in range(len(listOfInts)-2, -1, -1):
        rightIxProduct *= listOfInts[y+1]
        listOfProducts[y] *= rightIxProduct

    return listOfProducts

testList = [1,7,3,4]
print(get_products_of_all_ints_except_at_index2(testList))
