from Node import Node

def find_common_ancestor_top_down(root, x, y):
    if root is None:
        return None

    is_x_in_left = contains(root.left, x)
    is_y_in_right = contains(root.right, y)
    if is_x_in_left == is_y_in_right:
        return root

    if is_x_in_left:
        return find_common_ancestor_top_down(root.left, x, y)
    else:
        return find_common_ancestor_top_down(root.right, x, y)


def find_common_ancestor_bottom_up(root, x, y):
    if root is None:
        return None
    elif root is x:
        return x
    elif root is y:
        return y

    left_subtree_result = find_common_ancestor_bottom_up(root.left, x, y)
    if left_subtree_result is not None and left_subtree_result is not x and left_subtree_result is not y:
        return left_subtree_result

    right_subtree_result = find_common_ancestor_bottom_up(root.right, x, y)
    if right_subtree_result is not None and right_subtree_result is not x and right_subtree_result is not y:
        return right_subtree_result

    if left_subtree_result is None and right_subtree_result is None:
        return None
    elif left_subtree_result is None:
        return right_subtree_result
    elif right_subtree_result is None:
        return left_subtree_result
    else:
        return root

def contains(root, target):
    if root is target:
        return True
    elif root is None:
        return False
    else:
        return contains(root.left, target) or contains(root.right, target)


if __name__ == '__main__':

    node1 = Node(1)
    root = node1
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

    assert find_common_ancestor_top_down(root, node6, node7) is node3
    assert find_common_ancestor_top_down(root, node4, node7) is root

    assert find_common_ancestor_bottom_up(root, node6, node7) is node3
    assert find_common_ancestor_bottom_up(root, node4, node7) is root
