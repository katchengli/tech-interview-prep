class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


def kth_to_last_node(fromLast, rootNode):
    node = rootNode
    totalNodes = 0

    while node != None:
        totalNodes += 1
        node = node.next

    #initially forgot this error case
    if fromLast > totalNodes:
        raise ValueError('node needed is larger than the length of the linked list: %s' % fromLast)

    node = rootNode
    for i in range(totalNodes-fromLast):
        node = node.next

    return node



a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print(kth_to_last_node(2, a).value)
# returns the node with value "Devil's Food" (the 2nd to last node)
