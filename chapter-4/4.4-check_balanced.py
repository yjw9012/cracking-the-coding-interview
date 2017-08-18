from Node import Node

def check_balanced(root):
    if root is None:
        return (True, 0)

    is_left_subtree_balanced, left_subtree_height = check_balanced(root.left)
    if not is_left_subtree_balanced:
        return (False, -1)
    is_right_subtree_balanced, right_subtree_height = check_balanced(root.right)
    if not is_right_subtree_balanced:
        return (False, -1)

    if abs(left_subtree_height - right_subtree_height) > 1:
        return (False, -1)
    else:
        return (True, max(left_subtree_height, right_subtree_height) + 1)


if __name__ == '__main__':

    node1 = Node(1)
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

    assert check_balanced(node1)[0]

    node4.right = Node(8)

    assert not check_balanced(node1)[0]
