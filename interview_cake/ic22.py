class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

def delete_node(node):
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        raise Exception("Can't delete the last node with this method!") #<-- forgot this case! oops

delete_node(b)
print(a.value)
print(a.next.value)
print(a.next.next)

#Note: have to explain the side effects of this solution (if anything else points to the nodes....)
