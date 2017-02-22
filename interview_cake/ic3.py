#constraint: list_of_ints will always have at least 3 integers
#can have negative numbers

def highest_product_three_ints(list_of_ints):
    biggest_int = max(list_of_ints)
    list_of_ints.remove(biggest_int)

    max_int1 = max(list_of_ints)
    list_of_ints.remove(max_int1)
    max_int2 = max(list_of_ints)
    list_of_ints.remove(max_int2)

    if list_of_ints:
        min_int1 = min(list_of_ints)
        list_of_ints.remove(min_int1)
    else:
        return biggest_int * max_int1 * max_int2

    if list_of_ints:
        min_int2 = min(list_of_ints)
        #list_of_ints.remove(min_int2)
    else:
        min_int2 = max_int2

    potent_highest_product1 = biggest_int * min_int1 * min_int2
    potent_highest_product2 = biggest_int * max_int1 * max_int2

    if potent_highest_product1 > potent_highest_product2:
        return potent_highest_product1
    else:
        return potent_highest_product2

print(highest_product_three_ints([3, 4, 5, 6]))
#should return 120
print(highest_product_three_ints([-10, -10, 5, 6]))
#should return 600
print(highest_product_three_ints([-60, -100, -1, -2]))
#should return -120
print(highest_product_three_ints([600, 200, -1, -2]))
#should return 1200
print(highest_product_three_ints([1000, -1000, -1, 1]))
#should return 1000000
print(highest_product_three_ints([1000, -1000, -1, 1, 800]))
#should return 1000000
print(highest_product_three_ints([1000, -1000, -1, 1, -800]))
#should return 800000000
