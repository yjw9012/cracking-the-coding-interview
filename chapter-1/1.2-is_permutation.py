def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    dict = {}
    for char in s1:
        dict[char] = dict.get(char, 0) + 1

    for char in s2:
        if char not in dict or dict[char] == 0:
            return False

    return True

s1 = "abcde"
s2 = "bdcea"
print(is_permutation(s1, s2))

s2 = "bdzea"
print(is_permutation(s1, s2))
