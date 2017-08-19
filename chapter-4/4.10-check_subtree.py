from Node import Node

def is_subtree(t1, t2):
    if t2 is None:
        return True
    if t1 is None:
        return False

    if t1.data == t2.data and is_same(t1, t2):
        return True

    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)

def is_same(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    elif t1.data == t2.data:
        return is_same(t1.left, t2.left) and is_same(t1.right, t2.right)
    else:
        return False


if __name__ == '__main__':

    t1 = node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node5.left = node7

    t2 = other_node3 = Node(3)
    other_node5 = Node(5)
    other_node6 = Node(6)
    other_node7 = Node(7)

    other_node3.left = other_node5
    other_node3.right = other_node6
    other_node5.left = other_node7

    assert is_subtree(t1, t2)

    other_node5.left = None
    assert not is_subtree(t1, t2)
