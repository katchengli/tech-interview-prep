def findUnique(listOfDrones):
    dronesSet = set()
    for i in range(len(listOfDrones)):
        if listOfDrones[i] in dronesSet:
            dronesSet.remove(listOfDrones[i])
        else:
            dronesSet.add(listOfDrones[i])

    return dronesSet.pop()

#InterviewCake answer:

def find_unique_delivery_id(delivery_ids):

    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id
