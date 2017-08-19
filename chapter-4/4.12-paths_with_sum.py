from Node import Node

def count_paths_with_sum(root, target):
    if root is None:
        return 0

    count = 0
    q = []
    q.append(root)
    while len(q) > 0:
        node = q.pop(0)
        count += count_paths_with_sum_starting_at_node(node, target, [])
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

    return count

def count_paths_with_sum_starting_at_node(cur, target, path):
    if cur is None:
        return 0

    count = 0
    path.append(cur.data)
    if sum(path) == target:
        count += 1

    left_subtree_count = count_paths_with_sum_starting_at_node(cur.left, target, path)
    right_subtree_count = count_paths_with_sum_starting_at_node(cur.right, target, path)

    path.pop()
    return count + left_subtree_count + right_subtree_count


if __name__ == '__main__':

    root = node1 = Node(1)
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

    assert count_paths_with_sum(root, 3) == 2

    node1.data = node2.data = node3.data = node4.data = node5.data = node6.data = node7.data = 0
    assert count_paths_with_sum(root, 0) == 18

    node2.data = 1
    assert count_paths_with_sum(root, 0) == 14

    node2.data = -1
    assert count_paths_with_sum(root, -1) == 4
