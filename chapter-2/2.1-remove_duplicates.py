from Node import Node

def remove_dups(n):
    dict_count = {}
    cur = n
    while cur is not None:
        dict_count[cur.data] = dict_count.get(cur.data, 0) + 1
        cur = cur.next

    dups = set()
    for k, count in dict_count.items():
        if count > 1:
            dups.add(k)

    cur = n
    prev = None
    while cur is not None:

        if cur.data in dups:
            if cur is n:
                n = n.next
                cur = n
            else:
                prev.next = cur.next
                cur = cur.next
                continue

        prev = cur
        cur = cur.next

    return n

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

    n = remove_dups(node4)

    # Should be 1 -> 3
    n.print_node_list()

    assert n.data == 1
    assert n.next.data == 3
    assert n.next.next is None
