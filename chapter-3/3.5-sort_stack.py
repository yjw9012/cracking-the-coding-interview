def sort_stack(S):
    stack_helper = []

    while len(S) > 0:
        num = S.pop()
        count = 0
        while len(stack_helper) > 0 and stack_helper[-1] > num:
            S.append(stack_helper.pop())
            count += 1

        stack_helper.append(num)
        for i in range(count):
            stack_helper.append(S.pop())

    while len(stack_helper) > 0:
        S.append(stack_helper.pop())

S = [5,4,1,3,2]
sort_stack(S)
for i in range(1,6):
    assert S.pop() == i

# Misunderstood the problem:
class SortStack():

    def __init__(self):
        self.data = []
        self.stack = []

    def push(self, e):
        while not self.is_empty() and self.peek() < e:
            self.stack.append(self.data.pop())

        self.data.append(e)
        while len(self.stack) > 0:
            self.data.append(self.stack.pop())

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


S = SortStack()

S.push(5)
S.push(1)
S.push(2)
S.push(4)
S.push(3)

for i in range(1,6):
    assert S.pop() == i
