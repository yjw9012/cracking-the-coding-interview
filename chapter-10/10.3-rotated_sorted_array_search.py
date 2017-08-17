# Assuming arr contains unique numbers...
def binary_search_rotated(arr, target):
    return binary_search_rotated_recur(arr, target, 0, len(arr) - 1)

def binary_search_rotated_recur(arr, target, start, end):

    if start == end:
        if arr[start] == target:
            return start
        else:
            return -1
    elif start > end:
        return -1

    mid = (start + end) // 2
    mid_num = arr[mid]

    if mid_num == target:
        return mid

    if arr[start] < mid_num:
        # Left subarray is sorted
        if arr[start] <= target <= mid_num:
            return binary_search_rotated_recur(arr, target, start, mid - 1)
        else:
            return binary_search_rotated_recur(arr, target, mid + 1, end)
    else:
        # Right subarray is sorted
        if mid_num <= target <= arr[end]:
            return binary_search_rotated_recur(arr, target, mid + 1, end)
        else:
            return binary_search_rotated_recur(arr, target, start, mid - 1)


if __name__ == "__main__":

    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    assert binary_search_rotated(arr, 16) == 1
    assert binary_search_rotated(arr, 5) == 8
    assert binary_search_rotated(arr, 14) == len(arr) - 1
    assert binary_search_rotated(arr, -2) == -1
