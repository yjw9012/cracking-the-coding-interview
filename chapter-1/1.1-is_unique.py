def is_unique(s):
    char_set = set()

    for char in s:
        if char in char_set:
            return False
        char_set.add(char)

    return True

if __name__ == "__main__":
    s = "abcdefghiajk";
    assert not is_unique(s)

    s = "abcdefghijklmnop";
    assert is_unique(s)
