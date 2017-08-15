from Node import Node

def kth_to_last(head, k):
    pioneer = head
    for i in range(k):
        pioneer = pioneer.next

    runner = head
    while pioneer is not None:
        pioneer = pioneer.next
        runner = runner.next

    return runner.data

if __name__ == "__main__":

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(4)
    node6 = Node(2)

    node4.next = node1
    node1.next = node3
    node3.next = node5
    node5.next = node2
    node2.next = node6

    assert kth_to_last(node4, 2) == 2
    assert kth_to_last(node4, 4) == 3
