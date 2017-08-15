class MyQueue:

    def __init__(self):
        self.data1 = []
        self.data2 = []

    def enqueue(self, e):
        self.data1.append(e)

    def dequeue(self):
        if len(self.data2) > 0:
            return self.data2.pop()
        else:
            if len(self.data1) > 0:
                while len(self.data1) > 0:
                    self.data2.append(self.data1.pop())
                return self.data2.pop()
            else:
                raise Exception("Queue is empty")


Q = MyQueue()

Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)

for i in range(1,6):
    assert Q.dequeue() == i
