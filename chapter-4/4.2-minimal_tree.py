from Node import Node

def create_minimal_bst(arr):
    return create_minimal_bst_recur(arr, 0, len(arr) - 1)

def create_minimal_bst_recur(arr, start, end):
    if start > end:
        return None
    elif start == end:
        return Node(arr[start])

    mid = (start + end) // 2
    left_subtree = create_minimal_bst_recur(arr, start, mid - 1)
    right_subtree = create_minimal_bst_recur(arr, mid + 1, end)

    root = Node(arr[mid], left_subtree, right_subtree)
    return root

if __name__ == '__main__':

    arr = [1, 2, 4, 7, 9, 11, 14, 16]
    root = create_minimal_bst(arr)

    assert root.data == 7

    left_subtree = root.left
    right_subtree = root.right
    assert left_subtree.data == 2
    assert right_subtree.data == 11

    assert left_subtree.left.data == 1
    assert left_subtree.right.data == 4
    assert right_subtree.left.data == 9
    assert right_subtree.right.data == 14

    assert right_subtree.right.right.data == 16
