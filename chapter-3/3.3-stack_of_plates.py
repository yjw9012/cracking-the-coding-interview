class SetOfStacks:
    STACK_CAPACITY = 3

    def __init__(self):
        self.stacks = []

    def push(self, e):
        if self.is_empty():
            self.stacks.append([e])
            return

        if len(self.stacks[-1]) < SetOfStacks.STACK_CAPACITY:
            self.stacks[-1].append(e)
        else:
            self.stacks.append([e])

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        e = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return e

    def popAt(self, idx):
        if idx < 0:
            raise Exception("Invalid index")
        if len(self.stacks) <= idx:
            raise Exception("Stack at the index is empty")

        e = self.stacks[idx].pop()

        if len(self.stacks) > idx + 1:
            pop_count = self.size() - (idx + 1) * self.STACK_CAPACITY + 1
            stack = []
            for i in range(pop_count):
                stack.append(self.pop())
            while len(stack) > 0:
                self.push(stack.pop())
        else:
            if len(self.stacks[-1]) == 0:
                self.stacks.pop()

        return e

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stacks[-1][-1]

    def is_empty(self):
        return len(self.stacks) == 0

    def size(self):
        if self.is_empty():
            return 0
        return self.STACK_CAPACITY * (len(self.stacks) - 1) + len(self.stacks[-1])

if __name__ == "__main__":

    S = SetOfStacks()

    S.push(1)
    S.push(2)
    S.push(3)

    S.push(4)
    S.push(5)
    S.push(6)

    S.push(7)
    S.push(8)

    print(S.stacks)

    for i in range(8,0,-1):
        assert S.pop() == i

    assert S.is_empty()


    # Test case for Follow-up

    S = SetOfStacks()

    S.push(1)
    S.push(2)
    S.push(3)

    S.push(4)
    S.push(5)
    S.push(6)

    S.push(7)
    S.push(8)
    S.push(9)

    assert S.popAt(0) == 3
    print(S.stacks)

    assert S.popAt(1) == 7
    print(S.stacks)

    assert S.popAt(2) == 9
    print(S.stacks)
