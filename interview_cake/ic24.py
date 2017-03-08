class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


def reverseLinkedList(head):
    originalPointer = head
    newHead = None
    secondNew = None

    while originalPointer != None:
        newHead = originalPointer
        originalPointer = originalPointer.next
        newHead.next = secondNew
        secondNew = newHead
    return newHead

node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

newHead = reverseLinkedList(node1)

while newHead != None:
    print(newHead.value)
    newHead = newHead.next

print(reverseLinkedList(None))
print(reverseLinkedList(LinkedListNode(6)).value)
