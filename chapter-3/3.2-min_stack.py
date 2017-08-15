class Stack:

    def __init__(self):
        self.data = []

    def push(self, e):
        try:
            min_num = min(self.min(), e)
            self.data.append((e, min_num))
        except:
            self.data.append((e, e))

    def pop(self):
        if len(self.data) == 0:
            raise Exception("Stack is full!")
        return self.data.pop()[0]

    def min(self):
        if len(self.data) == 0:
            raise Exception("Stack is full")
        return self.data[-1][1]

if __name__ == "__main__":

    S = Stack()

    S.push(2)
    S.push(5)
    S.push(3)
    S.push(4)
    S.push(1)

    assert S.min() == 1
    assert S.pop() == 1

    assert S.min() == 2
    assert S.pop() == 4

    assert S.min() == 2
    assert S.pop() == 3

    assert S.min() == 2
    assert S.pop() == 5

    assert S.min() == 2
