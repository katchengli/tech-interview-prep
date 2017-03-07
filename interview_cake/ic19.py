class MyStacksQueue(object):
    def __init__(self):
        self.enqueueQ = list()
        self.dequeueQ = list()

    def enqueue(self, value):
        self.enqueueQ.append(value)
        return

    def dequeue(self):
        if len(self.dequeueQ) == 0 and len(self.enqueueQ) == 0:
             raise IndexError("Can't dequeue from empty queue!")
        elif len(self.dequeueQ) == 0:
            for _ in range(len(self.enqueueQ)):
                self.dequeueQ.append(self.enqueueQ.pop())

        return self.dequeueQ.pop()

q = MyStacksQueue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeueQ)
print(q.enqueueQ)
print(q.dequeue())
