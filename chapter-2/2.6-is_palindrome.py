from Node import Node

# Try using Stack

def is_palindrome(head):
    if head is None or head.next is None:
        return True

    stack = []
    fast_walk = slow_walk = head
    while fast_walk is not None and fast_walk.next is not None:
        stack.append(slow_walk.data)
        slow_walk = slow_walk.next
        fast_walk = fast_walk.next.next

    if fast_walk is not None:
        slow_walk = slow_walk.next

    while len(stack) > 0:
        data = stack.pop()
        if data != slow_walk.data:
            return False
        slow_walk = slow_walk.next

    return True

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

assert not is_palindrome(node1)

node4.data = 2
node5.data = 1

assert is_palindrome(node1)

node4.next = None
node3.data = 2
node4.data = 1
assert is_palindrome(node1)
