class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(Stack):
    def __init__(self):
        super().__init__()
        self.maxStack = Stack()

    # push a new item to the last index
    def push(self, item):
        if not self.items or self.maxStack.peek() < item:
            self.maxStack.push(item)

        super().push(item)

    # remove the last item
    def pop(self):
        popped = super().pop()
        if self.maxStack.peek() == popped:
            self.maxStack.pop()
        return popped

    def get_max(self):
        return self.maxStack.peek()

maxS = MaxStack()
print(maxS.get_max())
maxS.push(2)
print(maxS.get_max())
maxS.push(3)
print(maxS.get_max())
maxS.pop()
maxS.pop()
print(maxS.get_max())
