from Node import Node

def create_list_of_depths(root):
    if root is None:
        return []

    lists = []
    Q = []
    Q.append((root, 0))

    while len(Q) > 0:
        node, depth = Q.pop(0)

        if len(lists) <= depth:
            lists.append([])
        lists[depth].append(node.data)

        if node.left is not None:
            Q.append((node.left, depth+1))
        if node.right is not None:
            Q.append((node.right, depth+1))

    return lists


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

    lists = create_list_of_depths(node1)
    print(lists)
