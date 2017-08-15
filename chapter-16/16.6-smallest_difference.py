def get_smallest_diff(arr1, arr2):
    smallest_diff = 10000000
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            diff = abs(arr1[i] - arr2[j])
            if diff < smallest_diff:
                smallest_diff = diff

    return smallest_diff


def get_smallest_diff_better(arr1, arr2):
    smallest_diff = 10000000
    arr1.sort()
    arr2.sort()
    arr1_idx = 0
    arr2_idx = 0
    while arr1_idx < len(arr1) and arr2_idx < len(arr2):
        diff = abs(arr1[arr1_idx] - arr2[arr2_idx])
        if diff == 0:
            return 0
        if diff < smallest_diff:
            smallest_diff = diff
        if arr1[arr1_idx] < arr2[arr2_idx]:
            arr1_idx += 1
        else:
            arr2_idx += 1
    return smallest_diff

if __name__ == "__main__":

    arr1 = [1, 3, 15, 11, 2]
    arr2 = [23, 127, 235, 19, 8]

    assert get_smallest_diff_better(arr1, arr2) == 3
