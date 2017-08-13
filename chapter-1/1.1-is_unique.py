def is_unique(s):
    char_set = set()

    for char in s:
        if char in char_set:
            return False
        char_set.add(char)

    return True

s = "abcdefghiajk";
print(s + " is unique? " + str(is_unique(s)))

s = "abcdefghijklmnop";
print(s + " is unique? " + str(is_unique(s)))
