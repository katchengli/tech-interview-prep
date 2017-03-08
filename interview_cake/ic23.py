class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def contains_cycle(rootNode):
    pointer1 = rootNode
    pointer2 = rootNode

    while True:
        pointer1 = pointer1.next

        if pointer2.next != None:
            pointer2 = pointer2.next.next
        else:
            return False

        if pointer1 == pointer2:
            return True
        elif pointer2 == None:
            return False


node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(contains_cycle(node1))
node4.next = None
print(contains_cycle(node1))
