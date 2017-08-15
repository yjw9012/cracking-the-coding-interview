from Node import Node

def find_intersection(head1, head2):
    if head1 is None or head2 is None:
        return None

    node_set = set()
    walk = head1
    while walk is not None:
        node_set.add(walk)
        walk = walk.next

    walk = head2
    while walk is not None:
        if walk in node_set:
            return walk
        walk = walk.next

    return None

if __name__ == "__main__":

    node1 = head1 = Node(3)
    node2 = Node(1)
    node3 = Node(5)
    node4 = Node(9)
    node5 = Node(7)
    node6 = Node(2)
    node7 = Node(1)
    node8 = head2 = Node(4)
    node9 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    node8.next = node9
    node9.next = node5

    assert find_intersection(head1, head2).data == 7

# Follow-up: don't use any extra data structure
# Think about it...













def find_intersection_2(head1, head2):
    if head1 is None or head2 is None:
        return None

    len1 = len(head1)
    len2 = len(head2)

    longer_list_head = head1 if len1 > len2 else head2
    shorter_list_head = head1 if longer_list_head is head2 else head2
    for i in range(abs(len1 - len2)):
        longer_list_head = longer_list_head.next

    walk1, walk2 = longer_list_head, shorter_list_head
    while walk1 is not None:
        if walk1 is walk2:
            return walk1
        walk1 = walk1.next
        walk2 = walk2.next

    return None

if __name__ == "__main__":
    assert find_intersection_2(head1, head2).data == 7
